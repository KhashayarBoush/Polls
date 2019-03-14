from django.db import models
from django.utils import timezone
import datetime
import uuid

class Question(models.Model):
    text = models.CharField(max_length = 300)
    date = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    def __str__(self):
       return '%s, %s' % (self.text, self.date)


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    text = models.CharField(max_length =  300)
    vots = models.IntegerField(default=0)
    def __str__(self):
        return '%s, %s' % (self.vots, self.text)
