from django.urls import path
from .views import PictureListView, PictureCreateView

urlpatterns = [
    path('', PictureListView.as_view(), name='home'),
    path('new/', PictureCreateView.as_view(), name='newPicture'),
]
