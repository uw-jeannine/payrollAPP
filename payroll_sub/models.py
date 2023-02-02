from django.db import models
from datetime import datetime

# Create your models here.
class Employees(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=255)
    phonenumber = models.IntegerField(default=0)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField()
    branch = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    joineddate = models.DateTimeField(auto_now_add = True)
    salary = models.IntegerField(default=0)
    assurance = models.CharField(max_length=255)
    bankaccountno = models.CharField(max_length=255)

class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    phonenumber = models.IntegerField()
    last_update_by = models.CharField(max_length=255)
    last_updated  = models.DateTimeField()

class Department(models.Model):
    depart_name = models.CharField(max_length=255)
    last_update_by = models.CharField(max_length=255)
    last_updated  = models.DateTimeField()

class Payment(models.Model):
    account = models.IntegerField()
    payment_date = models.DateField()
    payment_period = models.IntegerField()
    last_payment_by = models.CharField(max_length=255)

class Message(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    datetime = models.DateField(default=datetime.now().date())


