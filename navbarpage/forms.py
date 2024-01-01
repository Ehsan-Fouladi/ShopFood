from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ["name", "phone", "subject", "email"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "data-constraints":"@Required"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "data-constraints":"@Required"}),
            "subject": forms.Textarea(attrs={"class": "form-control", "data-constraints":"@Required"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "data-constraints":"@Email @Required"}),
        }