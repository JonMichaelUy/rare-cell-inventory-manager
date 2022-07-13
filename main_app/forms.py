from django import forms
from .models import Unit

class UnitSearchForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = ['ABO', 'D']