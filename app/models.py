#!flask/bin/python
# -*- coding: utf-8 -*-

import datetime
import re
import uuid

from app import app, db

class JobAd(db.Model):
    hash = db.Column(db.String(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    ad_text = db.Column(db.Text)
    masculine_word_count = db.Column(db.Integer, default=0)
    feminine_word_count = db.Column(db.Integer, default=0)
    masculine_coded_words = db.Column(db.Text)
    feminine_coded_words = db.Column(db.Text)
    coding = db.Column(db.String())

    email = db.Column(db.Text)
    name = db.Column(db.Text)
    company = db.Column(db.Text)

    def __init__(self, text, name, company, email):
        self.hash = str(uuid.uuid4())

        self.ad_text = text.ad_text
        self.masculine_word_count = text.masculine_word_count
        self.feminine_word_count = text.feminine_word_count
        self.masculine_coded_words = text.masculine_coded_words
        self.feminine_coded_words = text.feminine_coded_words
        self.coding = text.coding

        self.name = name
        self.company = company
        self.email = email

        db.session.add(self)
        db.session.commit()

    def list_words(self):
        if self.masculine_coded_words == "":
            masculine_coded_words = []
        else:
            masculine_coded_words = self.masculine_coded_words.split(",")
        if self.feminine_coded_words == "":
            feminine_coded_words = []
        else:
            feminine_coded_words = self.feminine_coded_words.split(",")
        masculine_coded_words = self.handle_duplicates(masculine_coded_words)
        feminine_coded_words = self.handle_duplicates(feminine_coded_words)
        return masculine_coded_words, feminine_coded_words

    def handle_duplicates(self, word_list):
        d = {}
        l = []
        for item in word_list:
            if item not in d.keys():
                d[item] = 1
            else:
                d[item] += 1
        for key, value in d.items():
            if value == 1:
                l.append(key)
            else:
                l.append("{0} ({1} times)".format(key, value))
        return l
