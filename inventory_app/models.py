from django.db import models



# Create your models here.

class Warehouse(models.Model):
    name = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Vehicle','Vehicle'),
        ( "Women's Clothing & Shoes","Women's Clothing & Shoes"),
        ("Men's Clothing & Shoes","Men's Clothing & Shoes"),
        ('Furniture','Furniture'),
        ('Electronics','Electronics')
    )

    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category =models.CharField(max_length=200,null=True, choices=CATEGORY)
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name