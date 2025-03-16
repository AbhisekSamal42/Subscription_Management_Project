from django.core.mail import send_mail, EmailMultiAlternatives
from membership.models import *
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.timezone import now
from django.shortcuts import render, redirect, get_object_or_404
from datetime import timedelta
from rest_framework import generics
from membership.serializers import *
from membership.forms import *


def home_view(request):
       #Render the Home Page.
    return render(request, 'home.html')

def plans_view(request):
       #Render the Subscription Plans Page.
    plans = SubscriptionPlan.objects.all()
    return render(request, 'plans.html', {'plans': plans})

def members_view(request):
        #Render the Members List Page.
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})

def register_view(request):
        #Handle Member Registration via HTML Form.
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)

            if member.membership_type.duration == 'Monthly':
                member.end_date = member.start_date + timedelta(days=30)
            elif member.membership_type.duration == 'Quarterly':
                member.end_date = member.start_date + timedelta(days=90)
            elif member.membership_type.duration == 'Yearly':
                member.end_date = member.start_date + timedelta(days=365)

            member.save()

            # Send Welcome Email
            send_welcome_email(member)

            return redirect('confirmation', member_id=member.id)
    else:
        form = MemberForm()

    return render(request, 'register.html', {'form': form})

def confirmation_view(request, member_id):
       #Render Confirmation Page after Registration.
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'confirmation.html', {'member': member})


def send_welcome_email(member):
            #Sends a welcome email to the new member.
    subject = "Welcome to Our Subscription Service!"
    html_content = render_to_string('emails/welcome_email.html', {'member': member})
    plain_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=subject,
        body=plain_content,
        from_email='abhiseksamal36@gmail.com',
        to=[member.email],
    )
    email.attach_alternative(html_content, "text/html")
    email.send()


class SubscriptionPlanListCreateView(generics.ListCreateAPIView):
       #API View to list and create subscription plans.
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

class SubscriptionPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
        #API View to retrieve, update, and delete a specific subscription plan.
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

class MemberListCreateView(generics.ListCreateAPIView):
      #API View to list and create members with email notification on registration.
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
           #Handles auto-calculating end_date and sending email to new members.
        member = serializer.save()

        # Auto-set end_date based on membership_type duration
        if member.membership_type.duration == 'Monthly':
            member.end_date = member.start_date + timedelta(days=30)
        elif member.membership_type.duration == 'Quarterly':
            member.end_date = member.start_date + timedelta(days=90)
        elif member.membership_type.duration == 'Yearly':
            member.end_date = member.start_date + timedelta(days=365)

        member.save()

        # Send Welcome Email
        send_welcome_email(member)

class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
      #API View to retrieve, update, and delete a specific member.
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
