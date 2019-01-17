#!flask/bin/python
# -*- coding: utf-8 -*-

import re
import operator
import functools

from app import app
from app.wordlists import *

def de_hyphen_non_coded_words(word):
    if word.find("-"):
        for coded_word in hyphenated_coded_words:
            if word.startswith(coded_word):
                return [word]
        return word.split("-")
    return [word]

def clean_up_text(messy_text):
    text = re.sub("[\\s]", " ", messy_text, 0, 0)
    text = re.sub(u"[\.\t\,“”‘’<>\*\?\!\"\[\]\@\':;\(\)\./&]", " ", text, 0, 0)
    text = re.sub(u"[—–]", "-", text, 0, 0)
    return text.lower()

class Text:

    def __init__(self, ad_text):
        self.ad_text = ad_text
        self.analyse()

    def analyse(self):
        word_list = self.clean_up_word_list()
        self.extract_coded_words(word_list)
        self.assess_coding()

    def clean_up_word_list(self):
        word_list = filter(lambda x: x, clean_up_text(self.ad_text).split(" "))
        return functools.reduce(operator.concat, map(de_hyphen_non_coded_words, word_list))

    def extract_coded_words(self, advert_word_list):
        words, count = self.find_and_count_coded_words(advert_word_list,
            masculine_coded_words)
        self.masculine_coded_words, self.masculine_word_count = words, count
        words, count = self.find_and_count_coded_words(advert_word_list,
            feminine_coded_words)
        self.feminine_coded_words, self.feminine_word_count = words, count

    def find_and_count_coded_words(self, advert_word_list, gendered_word_list):
        gender_coded_words = [word for word in advert_word_list
            for coded_word in gendered_word_list
            if word.startswith(coded_word)]
        return (",").join(gender_coded_words), len(gender_coded_words)

    def assess_coding(self):
        coding_score = self.feminine_word_count - self.masculine_word_count
        if coding_score == 0:
            self.coding = "neutral"
        elif coding_score > 3:
            self.coding = "strongly feminine-coded"
        elif coding_score > 0:
            self.coding = "feminine-coded"
        elif coding_score < -3:
            self.coding = "strongly masculine-coded"
        else:
            self.coding = "masculine-coded"
