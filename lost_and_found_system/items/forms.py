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

# forms.py
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email = forms.EmailField(max_length=100, required=True, label="Your Email")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Your Message")
    phone_number = forms.CharField(max_length=15, required=False, label="Your Phone Number (Optional)")  # New field for phone number
    whatsapp_number = forms.CharField(max_length=15, required=False, label="Your WhatsApp Number (Optional)")  # New field for WhatsApp number




