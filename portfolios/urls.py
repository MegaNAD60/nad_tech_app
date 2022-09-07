from django.urls import path
from .views import HomePageView, PricingPageView

urlpatterns = [
    path('pricing/', PricingPageView.as_view(), name='pricing'),
    path('', HomePageView.as_view(), name='home'),
]