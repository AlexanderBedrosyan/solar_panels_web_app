from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name = 'common/home-page.html'


class AboutUs(TemplateView):
    template_name = 'common/about-us.html'

