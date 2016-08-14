#coding: utf-8
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class Date(models.Model): #사용자가 입력한 일과를 일별로 관리합니다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    daily = models.DateField()

    def __str__(self):
        return str(self.daily)

    def get_absolute_url(self):
        return reverse("profiles:schedule_detail",
                       kwargs={
                           "username" : self.user.username,
                           "year":str(self.daily).split('-')[0],
                           "month":str(self.daily).split('-')[1],
                           "day":str(self.daily).split('-')[2],
                            }
                        )

class ScheduleManager(models.Manager):
    def all(self):
        qs = super().filter()

class Schedule(models.Model): #사용자가 입력한 일과를 관리합니다.
        date = models.ForeignKey(Date)
        title = models.CharField(max_length=30)
        start_time = models.TimeField()
        finish_time = models.TimeField()
        content = models.TextField(max_length=200)

        def __str__(self):
            return str(self.title)
