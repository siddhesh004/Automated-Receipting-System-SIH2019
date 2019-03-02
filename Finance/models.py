from django.contrib.auth.models import AbstractUser
from django.core.validators import URLValidator
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=50, unique= True, default='')


class Customer(models.Model):
    customer_id=models.CharField(max_length=10)
    customer_name=models.CharField(max_length=20)
    customer_phone=models.IntegerField(default=0)
    customer_email = models.EmailField(max_length=50, default='')
    customer_address = models.TextField()
    Gender = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    customer_gender = models.CharField(max_length=6, choices=Gender, default='Male')


class ReceiptData(models.Model):
    invoice_no = models.IntegerField(default = 0, unique=True, primary_key=True)
    #vendor_name = models.CharField(max_length=100, default='')
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.CharField(max_length=10)
    amount = models.CharField(max_length=10)
    #commodity = models.CharField(max_length=500, default='')
    Mode = (
        ('Card', 'cash'),
        ('Cheque', 'cheque')
    )
    mode = models.CharField(max_length=6, choices=Mode, default='Cheque')
    card_no = models.IntegerField(default=0000000000000000)
    cheque_no = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=100, default='',blank=True)


class Items(models.Model):
    invoice_no=models.ForeignKey(ReceiptData, on_delete=models.CASCADE)
    item_name=models.CharField(max_length=20)
    quant = models.CharField(max_length=10)
    unit_price=models.CharField(max_length=10)
    total = models.CharField(max_length=10)

class Uploads(models.Model):
    description = models.CharField(max_length=255, blank=True)
    #document = models.FileField(upload_to='documents/')
    document = models.FileField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
