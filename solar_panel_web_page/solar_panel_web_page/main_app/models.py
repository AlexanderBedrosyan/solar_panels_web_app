from django.db import models
from .validators import IsItAPhoneNumber, DateChecker

# Create your models here.


class Consultation(models.Model):
    first_name = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    email = models.EmailField(
        blank=False,
        null=False
    )
    phone_number = models.CharField(
        max_length=100,
        validators=[IsItAPhoneNumber()],
        blank=False,
        null=False
    )
    consultation_datetime = models.DateTimeField(
        blank=False,
        null=False,
        validators=[DateChecker()]
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заглавие")
    description = models.TextField(verbose_name="Описание")
    image_url = models.URLField(max_length=500, verbose_name="URL на изображението")
    secondary_image_url = models.URLField(
        max_length=500,
        verbose_name="Допълнително изображение",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата на създаване")

    def __str__(self):
        return self.title