from django.db import models
from django.contrib.auth.models import AbstractUser

'''
Create profile app (first name, last name, data of birth, biography, contacts).
'''


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=100, unique=True)






