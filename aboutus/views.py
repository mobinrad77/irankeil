from django.shortcuts import render
from django.views.generic import TemplateView

class AboutusPageView(TemplateView):
    template_name = "aboutus.html"