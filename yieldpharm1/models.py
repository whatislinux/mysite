from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=32)

    def __str__(self):
        return self.name

    # class Mate:
    #     ordering=['id']


class Product(models.Model):
    name=models.CharField(max_length=32)
    cas_no=models.CharField(max_length=32)
    molecular_ormula=models.CharField(max_length=32)
    molecular_weight=models.FloatField()
    molecular_structure=models.CharField(max_length=128)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name