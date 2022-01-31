from django.db import models

#Model used to modelize towns as described in the subject.
class Town(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=25)
    population = models.IntegerField()
    average_age = models.FloatField()
    district_code = models.IntegerField()
    department_code = models.CharField(max_length=25)
    region_code = models.IntegerField()
    region_name = models.CharField(max_length=25)
    def __str__(self):
        return str(self.name) + " (" + str(self.department_code) + ")"