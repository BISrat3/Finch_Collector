from django.shortcuts import redirect, render
from re import template
from .models import Finch, Review, Rating, BirdList
# from django import template
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.urls import reverse
#...
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
        template_name ="home.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["birdlists"] = BirdList.objects.all()
            return context

class About(TemplateView):
        template_name ="about.html"

@method_decorator(login_required, name='dispatch')
class FinchList(TemplateView):
    template_name = "finches_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name, user= self.request.user)
            context["header"] = f"Searching for {name}"
        else:
         context["finches"] = Finch.objects.filter(user = self.request.user) # this is where we add the key into our context object for the view to use
         context ["header"] = "Finches"
        return context

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'age']
    template_name = "finches_create.html"
    # success_url = "/finches/"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FinchCreate, self).form_valid(form)
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
        review = request.POST.get("review")
        rating = request.POST.get("rating")
        finch = Finch.objects.get(pk=pk)
        Rating.objects.create(review=review, rating=rating, finch=finch)
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

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("finches_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


