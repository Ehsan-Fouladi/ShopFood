from . import views
from django.urls import path

app_name = "product"
urlpatterns = [
    path("gallery/", views.GalleryView.as_view(), name="gallery")
]
