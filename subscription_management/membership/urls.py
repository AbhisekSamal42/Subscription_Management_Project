from django.urls import path,include
from rest_framework.routers import DefaultRouter
from membership.views import *

router = DefaultRouter()
router.register('SubscriptionPlanViewSet',SubscriptionPlanViewSet,basename='SubscriptionPlanViewSet')
router.register('MemberViewSet',MemberViewSet,basename='MemberViewSet')

urlpatterns = [
    path('', include(router.urls)),
]