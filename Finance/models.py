from django.contrib.auth.models import AbstractUser
from django.core.validators import URLValidator
from django.db import models


class Company(models.Model):

    company_name = models.CharField(max_length=50, primary_key=True)
    logo = models.ImageField(upload_to = 'templates/assets/images/company', default = 'templates/assets/images/company/logo-text.png')


class User(AbstractUser):
    username = models.CharField(max_length=50, unique= True, default='')
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, default='', blank=True)


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
    company_name = models.CharField(max_length=50, blank=True, default='')


class ReceiptData(models.Model):
    invoice_no = models.IntegerField(default = 0, unique=True, primary_key=True)
    #vendor_name = models.CharField(max_length=100, default='')
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.CharField(max_length=10)
    amount = models.CharField(max_length=10)
    #commodity = models.CharField(max_length=500, default='')
    Mode = (
        ('Card', 'card'),
        ('Cheque', 'cheque')
    )
    mode = models.CharField(max_length=6, choices=Mode, default='Cheque')
    card_no = models.IntegerField(default=0000000000000000)
    cheque_no = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=100, default='',blank=True)

    company_name = models.CharField(max_length=50, blank=True, default='')

    original_filename = models.CharField(max_length=50, blank=True, default='')
    mailed_status = models.BooleanField(default=False)


class Items(models.Model):
    invoice_no=models.ForeignKey(ReceiptData, on_delete=models.CASCADE)
    item_name=models.CharField(max_length=20)
    quant = models.CharField(max_length=10)
    unit_price=models.CharField(max_length=10)
    total = models.CharField(max_length=10)
    company_name = models.CharField(max_length=50, blank=True, default='')
    status = models.BooleanField(default=False)


class Uploads(models.Model):
    description = models.CharField(max_length=255, blank=True)
    #document = models.FileField(upload_to='documents/')
    document = models.FileField(null=True, blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=50, blank=True, default='')

