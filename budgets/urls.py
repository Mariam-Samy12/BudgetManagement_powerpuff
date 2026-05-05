from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.budget_home, name='budget_home'),
    path('create/', views.manage_budget, name='create_budget'), 
    path('edit/<int:pk>/', views.manage_budget, name='edit_budget'), 
]