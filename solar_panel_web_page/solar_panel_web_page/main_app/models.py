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