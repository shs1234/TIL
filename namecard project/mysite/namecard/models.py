from django.db import models

# Create your models here.

class Namecard(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.CharField(max_length=20,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    category = models.CharField(max_length=20,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name