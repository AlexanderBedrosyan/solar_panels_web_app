from django.shortcuts import render
import smtplib
from email.message import EmailMessage
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from solar_panel_web_page.main_app.forms import ConsultationCreateForm
from solar_panel_web_page.main_app.models import Consultation, Project
from pathlib import Path
from dotenv import load_dotenv
import os
import requests
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)


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
    ordering = ['-created_at']  # Most recent projects first


class Contacts(CreateView):
    template_name = 'common/contacts.html'
    model = Consultation
    form_class = ConsultationCreateForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        """Изпраща известие чрез Formspree след успешно попълване."""
        response = super().form_valid(form)
        consultation = form.instance

        # 🔹 Formspree endpoint
        formspree_url = os.getenv("FORMSPREE_URL")
        if not formspree_url:
            raise ImproperlyConfigured("Не е зададен FORMSPREE_URL в .env файла!")

        # 🔹 Подготвяме съобщението (по-сбит вид)
        message = (
            f"📩 Нова заявка за консултация!\n\n"
            f"👤 {consultation.first_name} {consultation.last_name}\n"
            f"📧 {consultation.email}\n"
            f"📞 {consultation.phone_number}\n"
            f"🗓️ {consultation.consultation_datetime.strftime('%d.%m.%Y %H:%M')}\n\n"
            f"📝 {consultation.description[:250]}..."  # ако описанието е дълго
        )

        # 🔹 Данните, които ще се изпратят към Formspree
        data = {
            "name": f"{consultation.first_name} {consultation.last_name}",
            "email": consultation.email,
            "message": message,
        }

        try:
            r = requests.post(formspree_url, data=data, timeout=10)
            if r.status_code == 200:
                print("✅ Имейлът е изпратен успешно чрез Formspree!")
            else:
                print(f"⚠️ Formspree върна статус {r.status_code}: {r.text}")

        except requests.exceptions.RequestException as e:
            print("❌ Грешка при изпращане към Formspree:", e)

        return response


class PrivacyPolicy(TemplateView):
    template_name = 'others/privacy-policy.html'


class TermsOfUse(TemplateView):
    template_name = 'others/terms_of_use.html'


class CookiePolicy(TemplateView):
    template_name = 'others/cookie-policy.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'common/project_detail.html'
    context_object_name = 'project'
    pk_url_kwarg = 'id'

