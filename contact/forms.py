from django import forms

from contact.models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Your Name"}),
            'email': forms.EmailInput(attrs={'placeholder': "Your Email"}),
            'subject': forms.TextInput(attrs={'class': "w-100", 'placeholder': "Subject"}),
            'message': forms.Textarea(attrs={'rows': "8", 'placeholder': "Your Message"})
        }
