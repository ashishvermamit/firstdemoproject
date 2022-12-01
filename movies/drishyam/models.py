from django.db import models

# Create your models here.

class drishyamModel(models.Model):
    actor=models.CharField(max_length=200)
    review=models.CharField(max_length=500)

    def __str__(self):
        return self.actor