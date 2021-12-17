from django.db import models

# Create your models here.
class Person(models.Model):
    fullname = models.CharField(max_length=250)
    password =models.CharField(max_length=100)
    mobile_number =models.IntegerField()

    def __str__(self):
        return self.fullname