from django.db import models

# Create your models here.

class SalesData(models.Model):
    month = models.CharField(max_length=10)
    sales = models.IntegerField()
    