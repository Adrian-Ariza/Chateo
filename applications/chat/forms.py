from django import forms

class IniciarChatForm(forms.Form):
    receptor = forms.CharField(
        label='Nombre de usuario del receptor',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mensaje = forms.CharField(
        label='Mensaje inicial',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    def __init__(self, usuario_emisor=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario_emisor = usuario_emisor

    def clean(self):
        from applications.user.models import user  # ajusta si usas otro path
        cleaned_data = super().clean()
        nombre_receptor = cleaned_data.get("receptor")
        mensaje = cleaned_data.get("mensaje")

        if self.usuario_emisor.userName == nombre_receptor:
            self.add_error("receptor", "No puedes iniciar un chat contigo mismo.")
            return

        try:
            receptor = user.objects.get(userName=nombre_receptor)
        except user.DoesNotExist:
            self.add_error("receptor", "El usuario no existe.")
            return

        if not receptor.is_visble:
            self.add_error("receptor", "Este usuario no está disponible.")
            return

        cleaned_data["receptor_obj"] = receptor  