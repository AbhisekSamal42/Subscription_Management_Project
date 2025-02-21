from django import forms
from memberships.models import *

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        field = ['first_name','last_name','email']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['member', 'plan_name', 'price', 'start_date', 'end_date']
