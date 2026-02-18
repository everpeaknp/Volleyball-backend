from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.create_membership_application, name='membership_apply'),
]