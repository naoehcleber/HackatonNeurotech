from django import forms

class PacienteForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    idade = forms.IntegerField(label='Idade', min_value=0)
    peso = forms.DecimalField(label='Peso (kg)', max_digits=5, decimal_places=2)
    cpf = forms.CharField(label='CPF', max_length=14)

    