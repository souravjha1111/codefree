from django import forms
from .models import irisModel

class IrisDataForm(forms.ModelForm):
    class Meta:
        model = irisModel
        fields = '__all__'
