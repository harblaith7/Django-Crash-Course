
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Animals(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="animals")

    def __str__(self):
        return self.name
