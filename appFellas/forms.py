from django import forms
from django.forms import ModelForm

from appFellas.models import Image, User


class UploadImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.FileInput()
        }


class AuthorizationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['e_mail', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
