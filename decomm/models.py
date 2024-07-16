from django.db import models

# Create your models here.
class decomm(models.Model):
    ticket_type=[
        ('email','EMAIL'),
        ('ess','ESS'),
        ('itons','ITONS'),
        ('aorts','AORTS'),
    ]
    
    status_type=[
        ('active','ACTIVE'),
        ('inprogress','INPROGRESS'),
        ('completed','COMPLETED'),
        ('onhold','ONHOLD'),
        ('cancelled','CANCELLED'),
    ]
    
    requestor=models.CharField(max_length=1000,null=True, blank=True)
    requesteddate=models.DateField()
    requestedyear=models.IntegerField()
    devicename=models.CharField(max_length=1000)
    hardware=models.CharField(max_length=1000)
    model=models.CharField(max_length=1000)
    domain=models.CharField(max_length=1000)
    devicefunction=models.CharField(max_length=1000)
