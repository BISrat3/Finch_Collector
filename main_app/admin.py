from django.contrib import admin
from .models import Finch, Review, Rating, BirdList

admin.site.register(Finch)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(BirdList)
# Register your models here.
