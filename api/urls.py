from django.contrib import admin
from django.urls import path
from api.views import CustomerView


urlpatterns = [
    path('customers/',CustomerView.as_view(), name='customer')
]