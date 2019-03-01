from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from .models import ReceiptData, Customer


def send_receipt_message():
    recipients = []
    for user in ReceiptData.objects.all():
        recipients.append(user.email)
    # send_mail(
    #     subject='Finance Receipt',
    #     message='PFA finance receipt',
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=recipients,
    # )
    email = EmailMessage(subject='Finance Receipt', body='PFA finance receipt', from_email=settings.EMAIL_HOST_USER,
                         to=recipients)
    # email.attach(image1.name, image1.read(), image1.content_type)
    email.send()
