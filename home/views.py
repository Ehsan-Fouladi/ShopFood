from django.shortcuts import render
from django.views.generic import TemplateView 
from .models import Banner, MenuFood, MenuProducts, SpecialOffer
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Banners"] = Banner.objects.all().order_by("-create_at")
        context["MenuFoods"] = MenuFood.objects.all().order_by("-create")
        context["products"] = MenuProducts.objects.all().order_by("-created")
        context["Offers"] = SpecialOffer.objects.all()
        return context
    