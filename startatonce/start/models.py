from django.db import models
#import MySQLdb
# Create your models here.
class userTable(models.Model):
    name=models.CharField(max_length=255,default='')
    email=models.CharField(max_length=255,default='')
    password=models.CharField(max_length=255,default="")

    def __str__(self):
        return self.name+self.email

class bikeDB(models.Model):
    trip_id=models.CharField(max_length=11,default='')
    year=models.CharField(max_length=4,default='')
    month = models.CharField(max_length=11, default='')
    week = models.CharField(max_length=11, default='')
    day = models.CharField(max_length=11, default='')
    hour = models.CharField(max_length=11, default='')
    usertype = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255, default='')
    starttime = models.datetime(max_length=0, default='')
    stoptime = models.datetime(max_length=0, default='')
    tripduration = models.CharField(max_length=0, default='')
    temperature = models.CharField(max_length=255, default='')
    events = models.CharField(max_length=255, default='')
    from_station_id = models.CharField(max_length=20, default='')
    from_station_name = models.CharField(max_length=255, default='')
    latitude_start = models.CharField(max_length=255, default='')
    longitude_start = models.CharField(max_length=255, default='')
    dpcapacity_start = models.CharField(max_length=255, default='')
    to_station_id = models.CharField(max_length=20, default='')
    to_station_name = models.CharField(max_length=255, default='')
    latitude_end = models.CharField(max_length=255, default='')
    longitude_end = models.CharField(max_length=255, default='')
    dpcapacity_end = models.CharField(max_length=255, default='')

    class Meta:
        db_table='user'

class predictTrip(models.Model):
    day = models.CharField(max_length=11, default='')
    stoptime = models.datetime(max_length=0, default='')
    tripduration = models.CharField(max_length=0, default='')
    to_station_id = models.CharField(max_length=20, default='')