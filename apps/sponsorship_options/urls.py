from django.urls import path
from .views import SponsorshipPageView, submit_sponsorship_application

urlpatterns = [
    path('', SponsorshipPageView.as_view(), name='sponsorship-page'),
    path('apply/', submit_sponsorship_application, name='sponsorship-apply'),
]
