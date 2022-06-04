from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('finches/', views.FinchList.as_view(), name="finches_list"),
    path('finches/new/', views.FinchCreate.as_view(), name="finches_create"),
    path('finches/<int:pk>/', views.FinchDetail.as_view(), name="finches_detail"),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finches_update"),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="finches_delete"),
    path('finches/<int:pk>/ratings/new', views.RatingCreate.as_view(), name="rating_create"),
    path('birdlists/<int:pk>/finches/<int:finch_pk>/', views.BirdListFinchAssoc.as_view(), name="birdlist_finch_assoc"),
    path('accounts/signup', views.Signup.as_view(), name="signup")
]