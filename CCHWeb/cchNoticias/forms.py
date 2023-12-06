from django import forms
from .models import Comentario

class NoticiasForms(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = {'mensagem'}