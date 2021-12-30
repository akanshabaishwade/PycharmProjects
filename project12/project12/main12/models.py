from django.db import models

# Create your models here.

class ColourStore(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    type = models.CharField(max_length=3)


    def __str__(self):
        return str(self.name)
