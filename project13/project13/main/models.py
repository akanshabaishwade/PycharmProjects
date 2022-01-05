from django.db import models

# Create your models here.

class WeddingInvitation(models.Model):
    name = models.CharField(max_length=30)
    relation = models.CharField(max_length=30)
    gift_rating = models.FloatField()


    def __str__(self):
        return str(self.name)


