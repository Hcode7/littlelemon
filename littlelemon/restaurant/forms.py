from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['first_name', 'last_name', 'guest_number', 'comment']
