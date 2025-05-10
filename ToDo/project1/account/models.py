from django.db import models

# Create your models here.


class Account(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField( max_length=10)
    email=models.EmailField(max_length=254,unique=True)


def __str__(self):
    return self.username
 