from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.task

class Access(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    has_visited = models.BooleanField(default=False,null=True)

