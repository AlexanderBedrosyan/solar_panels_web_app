from django import forms
from .models import Consultation


class BaseConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'


class ConsultationCreateForm(BaseConsultationForm):
    class Meta(BaseConsultationForm.Meta):
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Първо име...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Електронна поща...'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон за връзка...'}),
            'consultation_datetime': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local',
                    'placeholder': 'Изберете дата и час...'
                }
            ),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание...'})
        }
        labels = {
            'first_name': 'Първо име',
            'last_name': 'Фамилия',
            'email': 'Електронна поща',
            'phone_number': 'Телефон за връзка',
            'consultation_datetime': 'Дата и час за консултация',
            'description': 'Причина за консултацията'
        }