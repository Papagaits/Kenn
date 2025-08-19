from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='requestors-dashboard'),
    path('requestor/', views.request_management, name='request_management'),
    path('request-history/', views.request_history, name='request-history'),
    path('account-management/', views.account_management, name='account_management')
    
]
