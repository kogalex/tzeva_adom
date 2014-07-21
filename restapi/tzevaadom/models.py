from django.db import models


class Area(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    time_to_run = models.IntegerField()


class City(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    area = models.ForeignKey(Area, related_name='cities')

    def __unicode__(self):
        return self.name


class Alarm(models.Model):
    area = models.ForeignKey(Area, related_name='alarms')
    started = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(null=True)

    @property
    def is_safe(self):
        return False
