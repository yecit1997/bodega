from django import forms
from .models import Usuario, CustomUserManager


class UserForms(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        # fields = '__all__'
        fields = ['nombre', 'apellido', 'email'] 




