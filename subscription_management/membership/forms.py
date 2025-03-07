from django import forms
from membership.models import *

class MemberForm(forms.ModelForm):
    """Form for registering new members."""
    
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone', 'address', 'membership_type', 'start_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        """Ensure the email is unique."""
        email = self.cleaned_data.get('email')
        if Member.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
