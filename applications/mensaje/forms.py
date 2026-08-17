
from django import forms
from .models import mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = mensaje
        fields = ['content']  
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje...'}),
        }
