from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Finch(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    age = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.review


class Rating(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.IntegerField(default=1)
    finch = models.ForeignKey(Finch, on_delete = models.CASCADE, related_name= "ratings")
    
    def __str__(self):
        return self.review

class BirdList(models.Model):

    name = models.CharField(max_length=300)
    finches = models.ManyToManyField(Finch)
    
    def __str__(self):
        return self.name