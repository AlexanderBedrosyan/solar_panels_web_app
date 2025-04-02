from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from solar_panel_web_page.main_app.forms import ConsultationCreateForm
from solar_panel_web_page.main_app.models import Consultation, Project


# Create your views here.
class HomePage(TemplateView):
    template_name = 'common/home-page.html'


class AboutUs(TemplateView):
    template_name = 'common/about-us.html'


class Services(TemplateView):
    template_name = 'common/services.html'


class Projects(ListView):
    model = Project
    template_name = 'common/projects.html'
    context_object_name = 'object_list'
    paginate_by = 3


class Contacts(CreateView):
    template_name = 'common/contacts.html'
    model = Consultation
    form_class = ConsultationCreateForm
    success_url = reverse_lazy('home-page')


class PrivacyPolicy(TemplateView):
    template_name = 'others/privacy-policy.html'


class TermsOfUse(TemplateView):
    template_name = 'others/terms_of_use.html'


class CookiePolicy(TemplateView):
    template_name = 'others/cookie-policy.html'

