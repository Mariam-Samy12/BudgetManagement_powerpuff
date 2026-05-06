from django.urls import path
from . import views

# شلنا الـ app_name مؤقتاً عشان يقرأ 'dashboard' مباشرة
urlpatterns = [
    path('', views.dashboard_view, name='dashboard'), 
]