from django.db import models

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    