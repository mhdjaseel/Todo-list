from django.db import models

class Todo(models.Model):
    item=models.CharField(max_length=200)

def __str__(self):
        return self.id