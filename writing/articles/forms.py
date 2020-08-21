from django import forms
from django.forms import ModelForm
from .models import Visitors


class RegisterForm(ModelForm):
    class Meta:
        model = Visitors
        fields = '__all__'
