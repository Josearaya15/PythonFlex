from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil


class PerfilCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'pais',
            'direccion',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'avatar': 'Foto de perfil',
            'pais': 'País',
            'direccion': 'Dirección',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        widgets = {
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese su dirección'}),
            'pais': forms.TextInput(attrs={'placeholder': 'Ej: Chile'}),
        }


class PerfilChangeForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Nueva contraseña",
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nueva contraseña'
        })
    )
    password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme su nueva contraseña'
        })
    )

    class Meta:
        model = Perfil
        fields = [
            'first_name',
            'last_name',
            'email',
            'avatar',
            'pais',
            'direccion',
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'avatar': 'Foto de perfil',
            'pais': 'País',
            'direccion': 'Dirección',
        }
        widgets = {
            'direccion': forms.TextInput(attrs={
                'placeholder': 'Ingrese su dirección',
                'class': 'form-control'
            }),
            'pais': forms.TextInput(attrs={
                'placeholder': 'Ej: Chile',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'correo@ejemplo.com',
                'class': 'form-control'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get("password1")

        # Si se ingresó una nueva contraseña, la guardamos correctamente
        if password1:
            user.set_password(password1)
        if commit:
            user.save()
        return user