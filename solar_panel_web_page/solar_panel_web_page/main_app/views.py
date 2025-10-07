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


class Contacts(CreateView):
    template_name = 'common/contacts.html'
    model = Consultation
    form_class = ConsultationCreateForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        """Изпраща email след като формата е успешно попълнена."""
        response = super().form_valid(form)
        consultation = form.instance

        user = os.getenv("MAIL_NAME")
        password = os.getenv("MAIL_PASSWORD")
        recipient = os.getenv("RECEPIENT")

        msg = EmailMessage()
        msg["From"] = user
        msg["To"] = recipient
        msg["Subject"] = "🧾 Нова заявка за консултация от сайта"

        msg.set_content(f"""
    Здравей, имаш нова заявка за консултация:

    👤 Име: {consultation.first_name} {consultation.last_name}
    📧 Имейл: {consultation.email}
    📞 Телефон: {consultation.phone_number}
    📅 Дата и час: {consultation.consultation_datetime}

    📝 Описание:
    {consultation.description}

    --- 
    Това съобщение е изпратено автоматично от формата на сайта.
            """)

        try:
            with smtplib.SMTP_SSL("smtp.abv.bg", 465, timeout=20) as server:
                server.login(user, password)
                server.send_message(msg)
            print("✅ Имейлът е изпратен успешно!")
        except smtplib.SMTPAuthenticationError as e:
            print("❌ SMTP грешка при логин:", e)
        except Exception as e:
            print("❌ Грешка при изпращане:", type(e).__name__, e)

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

