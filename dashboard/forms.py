from django import forms

class checkNumber(forms.Form):
	numero = forms.IntegerField(label='Número de Archivo', widget=forms.TextInput(attrs={'placeholder':'Por ej. 12345', 'autofocus':'autofocus'}))
