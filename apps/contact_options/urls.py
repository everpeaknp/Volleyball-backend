from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.create_contact_submission, name='contact_submit'),
]