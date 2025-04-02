from django.contrib import admin
from .models import Consultation, Project


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass