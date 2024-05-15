# forms.py

from django import forms

class FlightSearchForm(forms.Form):
    origin = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'city-autocomplete', 'placeholder': 'Flying from'}))
    destination = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'city-autocomplete', 'placeholder': 'Flying to'}))
    # departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # return_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    # adults = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Adults (18+)'}))
    # children = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Children (0-17)'}))
    # travel_class = forms.ChoiceField(choices=[('Economy', 'Economy class'), ('Business', 'Business class'), ('First', 'First class')])
