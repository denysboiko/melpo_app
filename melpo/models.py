from django.db import models

# Create your models here.
class Theater(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)


class Play(models.Model):
    title = models.CharField(max_length=200)
    theater = models.ForeignKey(Theater, related_name='theaters', on_delete=models.CASCADE)


class Show(models.Model):
    date = models.DateField()
    time = models.TimeField()
    price = models.CharField(max_length=200)
