from django.db import models

# Create your models here.
class Math(models.Model):
    name = models.CharField(max_length=10, )
    param1 = models.IntegerField()
    param2 = models.IntegerField()