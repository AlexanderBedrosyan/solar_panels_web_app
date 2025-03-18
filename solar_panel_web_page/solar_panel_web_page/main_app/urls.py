from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('about-us/', views.AboutUs.as_view(), name='about-us'),
    path('services/', views.AboutUs.as_view(), name='services'),
]