from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="student",null=True,blank=True)

    def __str__(self):
        return self.name