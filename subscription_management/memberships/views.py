from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from memberships.models import *
from memberships.serializers import *

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
