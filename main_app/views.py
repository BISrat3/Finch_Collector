from re import template
from .models import Finch, Review, Rating, BirdList
# from django import template
from django.shortcuts import redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.urls import reverse
#...
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
        template_name ="home.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["birdlists"] = BirdList.objects.all()
            return context
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

# class Finch:
#     def __init__ (self, name, image, age):
#         self.name = name 
#         self.image = image
#         self.age = age


# finches = [
#   Finch("House Finch", "https://www.allaboutbirds.org/guide/assets/photo/306327601-480px.jpg",
#           "10 years"),
#   Finch("Purple Finch",
#           "https://cuteparrots.com/wp-content/uploads/2020/03/67284151-480px.jpg.webp", 
#           "8 years"),
#   Finch("Zebra Finch", "https://lafeber.com/pet-birds/wp-content/uploads/2018/06/Zebra-Finch.jpg",
#           "9 years"),
#   Finch("American Goldfinch",
#           "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/306710541/1800",
#            "6 years"),
#   Finch("House Sparrow Finch",
#           "https://upload.wikimedia.org/wikipedia/commons/6/6e/Passer_domesticus_male_%2815%29.jpg", " 5 years"),
# ]

class FinchList(TemplateView):
    template_name = "finches_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
         context["finches"] = Finch.objects.all() # this is where we add the key into our context object for the view to use
         context ["header"] = "Finches"
        return context

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'age']
    template_name = "finches_create.html"
    # success_url = "/finches/"
    def get_success_url(self):
        return reverse('finches_detail', kwargs= {'pk': self.object.pk})

class FinchDetail(DetailView):
    model = Finch
    template_name = "finches_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["ratings"] = Rating.objects.all()
        context["birdlists"] = BirdList.objects.all()
        return context

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'age']
    template_name = "finches_update.html"
    # success_url = "/finches/"
    def get_success_url(self):
        return reverse('finches_detail', kwargs= {'pk':self.object.pk})

class FinchDelete(DeleteView):
    model = Finch
    template_name = "finches_delete.html"
    success_url = "/finches/"

class RatingCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        age = request.POST.get("age")
        finch = Finch.objects.get(pk=pk)
        Rating.objects.create(name=name, age=age, finch=finch)
        return redirect('finches_detail', pk=pk)

class BirdListFinchAssoc(View):

    def get(self, request, pk, finch_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            BirdList.objects.get(pk=pk).finches.remove(finch_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            BirdList.objects.get(pk=pk).finches.add(finch_pk)
        return redirect('home')
