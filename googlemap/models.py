from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
# Create your models here.

class User2bike(models.Model):
    bike_id = models.CharField(max_length=256)
    user = models.ForeignKey(User, related_name='bike',default=1)

class Bike(models.Model):
  name = models.CharField(max_length=256)
  lat = models.FloatField(default=0.0)
  lng = models.FloatField(default=0.0)
  available = models.BooleanField(default=False)
  user = models.ForeignKey(User,  related_name='own_bike', default=1)
  x = models.FloatField(default=0.0)
  y = models.FloatField(default=0.0)
  z = models.FloatField(default=0.0)
  uid = models.IntegerField(default=0)
