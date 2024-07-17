# forms.py

from django import forms
from .models import RoomDetails, Hosteller, RentHistory

class RoomDetailsForm(forms.ModelForm):
    class Meta:
        model = RoomDetails
        fields = '__all__'

class HostellerForm(forms.ModelForm):
    class Meta:
        model = Hosteller
        fields = '__all__'

class RentHistoryForm(forms.ModelForm):
    class Meta:
        model = RentHistory
        fields = '__all__'
