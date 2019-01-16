[![CircleCI](https://circleci.com/gh/fterrier/gender-decoder.svg?style=svg)](https://circleci.com/gh/fterrier/gender-decoder)

# gender-decoder

Gender Decoder is a simple  tool that checks the text of job ads to see if it includes any subtly gender-coded language.

By 'subtly gender-coded language' I mean language that reflects stereotypes about men and women, like women being more nurturing and men more aggressive. A 2011 research paper showed that subtly masculine-coded language in ads can put women off applying for jobs.

To be clear: I don't believe that the concepts with masculine-coded words are the exclusive preserve of men. I know that people of all genders can be innovative, reckless, self-reliant and/or unreasonable. But the stereotype our society has created of men says that they are much more likely to have these qualities. The same thing goes for women. Unfortunately, people with non-binary genders were not included in the original research.

For more info, or to use the tool:
http://gender-decoder.katmatfield.com

The analysis bit of this tool has been made into a Python package, by Richard Pope:
https://pypi.python.org/pypi/genderdecoder/0.3

If you're interested in Gender Decoder, you may also like Karen Schoellkopf's
https://www.hiremorewomenintech.com/


## Installation

Install virtualenv:

```
virtualenv venv
```

Activate the env and install dependencies:

```
source venv/bin/activate
pip install -r requirements.txt
```

## Running

### Local environment

First create a local database:

```
env $(cat .ENV | xargs) python db_create.py
```

Then to run:

```
env $(cat .ENV | xargs) gunicorn runsite:app
open https://localhost:8000
```

Use with browser-sync:

```
browser-sync start --proxy http://127.0.0.1:8000/ --files="app/templates/**, app/static/**"
open https://localhost:3000
```

## Run the tests

```
env $(cat .ENV | xargs) python tests.py
```
