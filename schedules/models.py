#coding: utf-8
from django.db import models
from django.conf import settings

class Date(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    daily = models.DateField()

class Schedule(models.Model):
        date = models.ForeignKey(Date)
        title = models.CharField(max_length=30)
        start_time = models.TimeField()
        finish_time = models.TimeField()
        content = models.TextField(max_length=200)

