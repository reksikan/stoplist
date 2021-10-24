from django.db import models

# Create your models here.


class Phone(models.Model):
    number = models.CharField(max_length=15, primary_key=True)
