from django.urls import path, include
from rest_framework.routers import DefaultRouter
from memberships.views import *

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]