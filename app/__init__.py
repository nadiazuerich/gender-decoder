from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.email import EmailSender

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.debug = True

db = SQLAlchemy(app)
email_sender = EmailSender(app.config['SENDGRID_API_KEY'])

from app import views
