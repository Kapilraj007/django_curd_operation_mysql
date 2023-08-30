from django import forms
from .models import RegistrationForm

class MyRegistraterForm(forms.ModelForm):
    class Meta:
        model = RegistrationForm
        fields = ["name","age","address","contact","email"]