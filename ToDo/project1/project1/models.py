from django.db import models

class Todo(models.Model):
    id=models.IntegerField(primary_key=True,max_length=100)
    item=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


def __str__(self):
        return self.item