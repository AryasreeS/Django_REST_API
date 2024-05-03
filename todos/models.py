from django.db import models

# # Create your models here.
# class Todo(models.Model):
#     content = models.TextField()


class User(models.Model):
    name=models.CharField(max_length=50)
    email =models.CharField(max_length=50)