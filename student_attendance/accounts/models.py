from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICE =[
        ("student","Student"),
        ("admin","Admin")
    ]
    email = models.CharField(max_length=30,unique=True)
    phone = models.CharField(max_length=12,unique=True)
    role = models.CharField(choices=ROLE_CHOICE,max_length=20,default="student")

    def __str__(self):
        return self.username
