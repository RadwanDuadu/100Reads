from django import forms
from .models import Contact


# Form to handle user contact messages
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
