from django import forms
from .models import usuarios


class usuarioform(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = '__all__'