from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
    publish_date=models.DateField()
    publish=models.ForeignKey('Publish',models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class Publish(models.Model):
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)

    def __str__(self):
        return self.name



class Author(models.Model):
    name=models.CharField(max_length=32)