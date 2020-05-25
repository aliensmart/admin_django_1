from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=10, null=True)
    birth_date = models.DateField(blank=True, null=True)

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=6)