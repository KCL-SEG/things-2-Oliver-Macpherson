"""Forms of the project."""

from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea()}


    # name = forms.CharField(label="Name", max_length=35)
    # description = forms.CharField(label="Description", max_length=120, required=False, widget=forms.Textarea())
    # quantity = forms.CharField(label="Quantity", validators=[MinValueValidator(0), MaxValueValidator(50)], widget=forms.NumberInput())
