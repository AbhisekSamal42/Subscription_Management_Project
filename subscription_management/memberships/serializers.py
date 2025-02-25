from rest_framework import serializers
from memberships.models import *

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined']

class SubscriptionSerializer(serializers.ModelSerializer):
    member = MemberSerializer()

    class Meta:
        model = Subscription
        fields = ['id', 'member', 'plan_name', 'price', 'start_date', 'end_date']
