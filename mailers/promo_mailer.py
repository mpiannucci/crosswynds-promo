from google.appengine.api import mail
import config

def send_test_email(user_email):
    subject = "Test Email"
    body = "This is a test email from the prelaunch website!"
    mail.send_mail(config.application_email, user_email, subject, body)

def send_signup_email(user_email, referral_id):
    subject = "Crosswynds Traders Prelaunch"
    referal_url = config.base_url + referral_id
    body = """
Hi!! Thank you for signing up for Crosswynds Traders Prelaunch!! 

Don't leave your friends on the beach, share the link below with your friends to include them in the fun! Don't forget to check back and see what you've earned!

%s

Sincerely, 
Crosswynds Traders
""" % referal_url

    mail.send_mail(config.application_email, user_email, subject, body)