from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("<slug:slug>/", views.DetailView.as_view(), name="detail"),
    path("category/<int:pk>", views.category_view, name="categories"),
]
