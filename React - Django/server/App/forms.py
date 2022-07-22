from django import forms
 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
from .models import Etudiant
 
 
class EtudiantRegistration(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields =['EtudiantClass', 'EtudiantName'] 