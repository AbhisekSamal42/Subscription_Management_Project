from django.urls import path,include
from membership.views import *

urlpatterns = [
    # Template-Based Views

    path('', home_view, name='home'),
    path('plans/', plans_view, name='plans'),
    path('members/', members_view, name='members'),
    path('register/', register_view, name='register'),
    path('confirmation/<int:member_id>/', confirmation_view, name='confirmation'),

    # API Views
    
    path('api/plans/', SubscriptionPlanListCreateView.as_view(), name='api-plans-list'),
    path('api/plans/<int:pk>/', SubscriptionPlanDetailView.as_view(), name='api-plans-detail'),
    path('api/members/', MemberListCreateView.as_view(), name='api-members-list'),
    path('api/members/<int:pk>/', MemberDetailView.as_view(), name='api-members-detail'),
]