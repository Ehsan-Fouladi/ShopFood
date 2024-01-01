from . import views
from django.urls import path

app_name = "page"
urlpatterns = [
    path("contacts/", views.ContactView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
]
