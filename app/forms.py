from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, validators

class JobAdForm(FlaskForm):
    texttotest = TextAreaField(u'', [validators.Length(min=1)])
    name = StringField(u'Name', [validators.required()])
    company = StringField(u'Company', [validators.required()])
    email = StringField(u'Email', [validators.required(), validators.Email()])
