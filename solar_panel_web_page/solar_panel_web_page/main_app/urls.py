from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('about-us/', views.AboutUs.as_view(), name='about-us'),
    path('services/', views.Services.as_view(), name='services'),
    path('projects/', views.Projects.as_view(), name='projects'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('privacy-policy/', views.PrivacyPolicy.as_view(), name='privacy-policy'),
    path('terms-of-use/', views.TermsOfUse.as_view(), name='terms-of-use'),
    path('cookie-policy/', views.CookiePolicy.as_view(), name='cookie-policy'),
    path('project-detail/<int:id>', views.ProjectDetailView.as_view(), name='project-detail'),
]