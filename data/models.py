from django.db import models

# Create your models here.

class Town(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=25)
    population = models.IntegerField()
    average_age = models.FloatField()
    district_code = models.IntegerField()
    department_code = models.CharField(max_length=25)
    region_code = models.IntegerField()
    region_name = models.CharField(max_length=25)