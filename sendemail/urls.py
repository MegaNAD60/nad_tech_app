from django.contrib import admin
from django.urls import path

from .views import contactView, successView

app_name = "portfolios"

urlpatterns = [
    path('home/', contactView, name='home'),
    path('success/', successView, name='success'),
]