from django.db import models

# Create your models here.
class Finch(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    age = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']