from django.db import models

# Create your models here.
from django.db import models

class ShirtColor(models.Model):
    color = models.CharField(max_length=20, unique=True)
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.color} - {self.frequency}"
