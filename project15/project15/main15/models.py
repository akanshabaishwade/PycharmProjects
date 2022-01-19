from django.db import models

# Create your models herec




class StudentData(models.Model):
    name = models.CharField(max_length=30)
    Class = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return str (self.Class)