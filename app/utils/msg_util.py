from twilio.rest import Client

from django.conf import settings
from django.core.mail import send_mail

from app.utils.log import log


def send_msg(msg, cell):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(messaging_service_sid=settings.TWILIO_MESSAGING_SERVICE_SID,
                               body=msg,
                               to=cell)
        return True
    except:
        log(f"Cannot send msg to: {cell}", "send_msg")
        return False


def send_email(title, msg, recipient_list):
    try:
        send_mail(subject=title,
                  message=msg,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=recipient_list)
        return True
    except:
        log(f"Cannot send email to: {recipient_list}", "send_msg")
        return False
