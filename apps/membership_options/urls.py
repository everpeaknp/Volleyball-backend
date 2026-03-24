from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.create_membership_application, name='membership_apply'),
    path('renew/', views.create_membership_renewal, name='membership_renew'),
]