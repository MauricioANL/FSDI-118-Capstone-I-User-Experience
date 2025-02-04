from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, forms

def home(request):

    pictureList = models.Picture.objects.all()

    return render(request,'home.html',{'listPicture': pictureList})

def newPicture(request):

    if request.method == 'POST':
        form = forms.PictureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.PictureForm()

    return render(request, 'newPicture.html', {'form': form})

# Create your views here.
