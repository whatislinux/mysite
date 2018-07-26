from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=200)
    name_en=models.CharField(max_length=200)
    def __str__(self):
        return self.name

    # class Mate:
    #     ordering=['id']


class Product(models.Model):
    name=models.CharField(max_length=200)
    name_en=models.CharField(max_length=200)
    cas_no=models.CharField(max_length=200)
    molecular_formula=models.CharField(max_length=200)
    molecular_weight=models.FloatField()
    molecular_structure=models.CharField(max_length=200)
    is_advantage_product=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name