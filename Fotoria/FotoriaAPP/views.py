
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Picture
from .forms import PictureForm

class PictureListView(ListView):
    model = Picture
    template_name = 'home.html'  
    context_object_name = 'listPicture'  

class PictureCreateView(CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'newPicture.html'
    success_url = reverse_lazy('home')

