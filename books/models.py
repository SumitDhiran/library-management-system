# Create your models here.
from turtle import title
from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date

from django.db.models.deletion import SET_NULL
# Create your models here.

class Book(models.Model):
    user        = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    title       =  models.CharField(max_length=200)
    author      =  models.CharField(max_length=200)
    publisher   =  models.CharField(max_length=200)
    sum_pages   =  models.IntegerField(null=True,blank=True)
    created  =  models.DateTimeField(auto_now_add=True)
    id       =  models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):

        return self.title


