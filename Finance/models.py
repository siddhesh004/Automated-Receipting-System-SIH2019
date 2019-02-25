from django.contrib.auth.models import AbstractUser
from django.core.validators import URLValidator
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=50, unique= True, default='')

class ReceiptData(models.Model):
    invoice_no = models.IntegerField(default = 0, unique=True)
    vendor_name = models.CharField(max_length=100, default='')
    date = models.DateField()
    amount = models.IntegerField(default=0)
    commodity = models.CharField(max_length=500, default='')
    Mode = (
        ('card', 'Cash'),
        ('cheque', 'Cheque')
    )
    mode = models.CharField(max_length=6, choices=Mode, default='Cheque')
    card_no = models.IntegerField(default=0000000000000000)
    cheque_no = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=100, default='')

class Uploads(models.Model):
    description = models.CharField(max_length=255, blank=True)
    #document = models.FileField(upload_to='documents/')
    document = models.FileField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
