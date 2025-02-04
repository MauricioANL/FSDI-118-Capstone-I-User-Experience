from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newPicture', views.newPicture, name='newPicture'),
]