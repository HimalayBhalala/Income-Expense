from django.core.mail import EmailMessage
from django.conf import settings

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(from_email=settings.EMAIL_HOST_USER,body=data['email_body'],subject=data['email_subject'],to=data['to'])
        email.send()