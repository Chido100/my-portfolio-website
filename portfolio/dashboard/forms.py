from django import forms
from .models import ContactMe



class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']