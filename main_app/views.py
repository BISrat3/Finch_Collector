from django import template
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):

        template_name ="home.html"
    # Here we are adding a method that will be ran when we are dealing with a GET request
    # def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express

class About(TemplateView):

    # Here we are adding a method that will be ran when we are dealing with a GET request
    # def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        # return HttpResponse("Finch About")
        template_name ="about.html"

class Finch:
    def __init__ (self, name, image, age):
        self.name = name 
        self.image = image
        self.age = age


finches = [
  Finch("House Finch", "https://www.allaboutbirds.org/guide/assets/photo/306327601-480px.jpg",
          "10 years"),
  Finch("Purple Finch",
          "https://cuteparrots.com/wp-content/uploads/2020/03/67284151-480px.jpg.webp", 
          "8 years"),
  Finch("Zebra Finch", "https://lafeber.com/pet-birds/wp-content/uploads/2018/06/Zebra-Finch.jpg",
          "9 years"),
  Finch("American Goldfinch",
          "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/306710541/1800",
           "6 years"),
  Finch("House Sparrow Finch",
          "https://upload.wikimedia.org/wikipedia/commons/6/6e/Passer_domesticus_male_%2815%29.jpg", " 5 years"),
]

class FinchList(TemplateView):
    template_name = "finches_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finches"] = finches # this is where we add the key into our context object for the view to use
        return context
