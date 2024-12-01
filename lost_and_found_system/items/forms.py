from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'date_lost_or_found', 'location', 'photo','status']


class ReportItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'date_lost_or_found', 'location', 'photo','status']

