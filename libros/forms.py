from django import forms
from admins.models import Autor

class NewBookForm(forms.Form):
    titulo = forms.CharField(
        max_length=100,
        initial='La mancha',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el título del libro',
                'class': 'form-control',
                'id': 'titulo',
            }
        )
    )
    editorial = forms.CharField(max_length=100)
    volumen = forms.IntegerField(initial=1)
    paginas = forms.IntegerField(initial=100, label='Nro. de páginas')
    edicion = forms.IntegerField(initial=1)
    # autores_choices = Autor.objects.all()
    # CHOICE_AUTORES = []
    # for a in autores_choices:
    #     CHOICE_AUTORES.append((a.id, a.persona)) # value, texto
    autor = forms.MultipleChoiceField(
        choices=((a.id, a.persona) for a in Autor.objects.all()),
        widget=forms.SelectMultiple(attrs={'size': '10'}),
        label='Autores'
    )

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if titulo == '':
            raise forms.ValidationError("El título no puede estar vacío")
        return titulo
