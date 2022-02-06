from email.policy import default
from django import forms
from django.core.exceptions import ValidationError


def int_sep_by_comma(value):
    vals_separated = value.split(',')
    for val in vals_separated:
        if val.isdigit() == False:
            raise ValidationError('Values must only be integers and cannot contain spaces.')

class PickYourData(forms.Form):
    your_data = forms.CharField(required=True, label='Enter your data:', max_length=50, validators=[int_sep_by_comma])
    # start_sim = forms.CharField(required=False, initial={'start_sim': 'simulate'})
    
# class StartSimulation(forms.Form):
#     start_sim = forms.CharField(required=False, initial={'start_sim': 'simulate'})