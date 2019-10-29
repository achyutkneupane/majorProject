from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    roll = models.CharField(max_length=15)
    contact = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/members/')
    class Meta:
        ordering = ['roll',]