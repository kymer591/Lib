from django import forms

class EditPersonaForm(forms.Form):
    direccion = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(max_value=99999999, min_value=10000000, required=True)
    email = forms.EmailField(required=True) # widget