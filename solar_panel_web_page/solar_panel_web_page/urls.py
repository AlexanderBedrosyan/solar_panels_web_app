from django.contrib import admin
from django.urls import path, include
from django.http import FileResponse
import os
from django.conf import settings


def sitemap_view(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'sitemap.xml')
    return FileResponse(open(file_path, 'rb'), content_type='application/xml')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('solar_panel_web_page.main_app.urls')),
    path('sitemap.xml', sitemap_view, name='sitemap'),
]
