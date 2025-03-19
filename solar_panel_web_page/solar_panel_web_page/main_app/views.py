from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name = 'common/home-page.html'


class AboutUs(TemplateView):
    template_name = 'common/about-us.html'


class Services(TemplateView):
    template_name = 'common/services.html'


class Projects(TemplateView):
    template_name = 'common/projects.html'


class Contacts(TemplateView):
    template_name = 'common/contacts.html'

