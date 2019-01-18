from flask import Flask
from flask import render_template, redirect, request
from app import app, db, email_sender
from app.forms import JobAdForm
from app.models import JobAd
from app.text import Text

def send_email(recipient, data):
    app.logger.info('Sending email to %s, with job ad: %s', recipient, data['hash'])
    from_email = "decoder@witty.works"
    subject = "New job ad received from " + data['email']
    content = """
        Name: {name}
        Company: {company}
        Email: {email}

        Text: {text}

        Hash: {hash}
        """.format(**data)

    try:
        email_sender.send_email(from_email, subject, recipient, content)
        app.logger.info('Email to %s sent succesfully: %s', recipient, data['hash'])
    except Exception as e: # this should not catch all exceptions but I have no idea how to do python
        app.logger.error('Could not send emails to %s with job ad: %s, exception: %s', recipient, data['hash'], e)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = JobAdForm()
    if request.method == "POST" and form.validate_on_submit():
        text = Text(form.texttotest.data)
        ad = JobAd(text, form.name.data, form.company.data, form.email.data)

        send_email(app.config['EMAIL_TO_NOTIFY'], dict(text = ad.ad_text, name = ad.name, company = ad.company, email = ad.email, hash=ad.hash));

        return redirect('results/{0}'.format(ad.hash))
    return render_template('home.html', form=form)


@app.route('/results/<ad_hash>')
def results(ad_hash):
    job_ad = JobAd.query.get_or_404(ad_hash)
    masculine_coded_words, feminine_coded_words = job_ad.list_words()
    return render_template('results.html', job_ad=job_ad,
        masculine_coded_words=masculine_coded_words,
        feminine_coded_words=feminine_coded_words)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
