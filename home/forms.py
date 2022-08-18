from django import forms

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }
        labels = {
            'p_name': 'NAME:',
            'p_phone': 'PHONE:',
            'p_mail': 'EMAIL:',
            'Doc_name': 'DOCTOR NAME:',
            'booking_date': 'BOOKING DATE'
        }
