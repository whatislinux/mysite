from django.db import models

# Create your models here.

class Car(models.Model):
    manufacturer=models.ForeignKey('Manufacturer',on_delete=models.CASCADE,)

class Manufacturer(models.Model):
    pass