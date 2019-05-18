from django.db import models

# Create your models here.


class Wardrobe(models.Model):
    email = models.CharField(max_length=30)
    clothes = models.CharField(max_length=20)
