import sendgrid
from sendgrid.helpers.mail import *

class EmailSender():

    def __init__(self, api_key):
        self.sg = sendgrid.SendGridAPIClient(apikey=api_key)

    def send_email(self, from_email, subject, to_email, content):
        mail = Mail(
            Email(from_email),
            subject,
            Email(to_email),
            Content("text/plain", content)
        )
        response = self.sg.client.mail.send.post(request_body=mail.get())
