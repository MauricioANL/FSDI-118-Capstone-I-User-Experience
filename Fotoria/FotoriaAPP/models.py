from django.db import models

# Create your models here.

class Picture(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    # urlimg = models.URLField()
    img = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.name
