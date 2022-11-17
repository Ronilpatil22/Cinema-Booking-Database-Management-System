from django.db import models

# Create your models here.
class contact(models.Model):
    username=models.CharField(max_length=10,default='Anonymous User')
    First_name=models.CharField(max_length=150)
    Last_name=models.CharField(max_length=150)
    Email_id=models.EmailField()
    Mobile_number=models.CharField(max_length=10)
    Message=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.username
class email_id(models.Model):
    email=models.EmailField()
    date=models.DateField()
    
class ticket(models.Model):
    username=models.CharField(max_length=10,default='Anonymous User')
    movie=models.CharField(max_length=150)
    date=models.DateField()
    seat=models.CharField(max_length=2,default='A1')
    screen=models.IntegerField(default='1')
    price=models.IntegerField(default='0')
    
    def __str__(self):
        return self.username

class movie(models.Model):
    name=models.CharField(max_length=150)
    time=models.TimeField()
    releasedate=models.DateField()
    about=models.CharField(max_length=5000)
    starcast=models.CharField(max_length=5000)