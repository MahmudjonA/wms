from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['warehouse', 'zone', 'aisle', 'rack', 'bin']
        widgets = {
            'warehouse': forms.Select(attrs={'class': 'form-control'}),
            'zone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zone'}),
            'aisle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aisle'}),
            'rack': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rack'}),
            'bin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bin'}),
        }
