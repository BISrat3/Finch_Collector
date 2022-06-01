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