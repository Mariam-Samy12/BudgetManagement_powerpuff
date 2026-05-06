from django.urls import path
from . import views

urlpatterns = [
    path('', views.financial_report, name='reports'),
]