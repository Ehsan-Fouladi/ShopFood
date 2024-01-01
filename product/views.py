from django.shortcuts import render
from django.views.generic import ListView
from .models import Gallery

class GalleryView(ListView):
    template_name  = "product/gallery.html"
    model = Gallery
    paginate_by = 9