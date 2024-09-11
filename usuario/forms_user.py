from django import forms
from .models import Usuario


class UserForms(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        # fields = '__all__'
        fields = ['nombre', 'apellido', 'email'] 
        
        
class EditPerfilUserForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email'] 

        
class EditUserForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','is_active', 'is_staff', 'is_superuser'] 
        widgets = {
            'nombre': forms.TextInput(attrs={'readonly': 'readonly'}),
        }




