from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)

class Department(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    contactno=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    AUTHUSER = models.OneToOneField(User, on_delete=models.CASCADE)


class Review(models.Model):
    date=models.DateField()
    review=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)

class Complaint(models.Model):
    date=models.DateField()
    complaint=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    priority=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)
    latitude=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)
    DEPARTMENT=models.ForeignKey(Department,on_delete=models.CASCADE)