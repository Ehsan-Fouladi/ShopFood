from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, TemplateView, DetailView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import AboutModel, OurStory, OurPartners, OurTeam

class ContactView(FormView):
    template_name = "navbarpage/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AboutView(ListView):
    template_name = "navbarpage/about.html"
    model = AboutModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Story"] = OurStory.objects.all()
        context["Partners"] = OurPartners.objects.all()
        context["Team"] = OurTeam.objects.all().order_by("-create_at")
        return context

class TeamView(ListView):
    template_name = "navbarpage/team.html"
    model = OurTeam

class ProfileTeamView(DetailView):
    template_name = "navbarpage/member-profile.html"
    model = OurTeam