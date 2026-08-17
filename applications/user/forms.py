from django import forms
from django.contrib.auth.hashers import make_password
from .models import user

class Loginuser(forms.Form):
    userName= forms.CharField(label='Usuario', 
    widget=forms.TextInput(attrs={'class': 'form-control textt2', 'rows': 3}))
    password = forms.CharField(
    label='Contraseña',
    widget=forms.PasswordInput(attrs={'class': 'form-control textt2', 'rows': 3})
    )
   
class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(
    label='Contraseña',
    widget=forms.PasswordInput(attrs={'class': 'form-control textt2', 'rows': 3}),
    help_text="Mínimo 8 caracteres"
    )
    password2 = forms.CharField(
    label='Confirmar Contraseña',
    widget=forms.PasswordInput(attrs={'class': 'form-control textt2', 'rows': 3})
    )
    class Meta:
        model = user
        fields = ['name', 'userName', 'email', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control textt2'}),
            'userName': forms.TextInput(attrs={'class': 'form-control textt2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control textt2'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control textt2'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        if len(password1) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class EditUserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control textt2'}),
        }

class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(
        label='Contraseña actual',
        widget=forms.PasswordInput(attrs={'class': 'form-control textt2'})
    )
    new_password = forms.CharField(
        label='Nueva contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control textt2'})
    )
    confirm_password = forms.CharField(
        label='Confirmar nueva contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control textt2'})
    )
    def clean(self):
        cleaned_data = super().clean()
        new = cleaned_data.get("new_password")
        confirm = cleaned_data.get("confirm_password")

        if new and confirm and new != confirm:
            self.add_error("confirm_password", "Las nuevas contraseñas no coinciden.")