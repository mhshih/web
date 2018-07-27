from django.db import models

# Create your models here.
class Collocation(models.Model):
    keyword=models.CharField(max_length=200)
    collocate=models.CharField(max_length=200)
