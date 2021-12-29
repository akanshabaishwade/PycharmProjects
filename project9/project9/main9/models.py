from django.db import models

# Create your models here.

class Friends(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return str(self.name)

