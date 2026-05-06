from django.urls import path
from . import views

urlpatterns = [
    path('', views.goals_list, name='goals_list'),
    path('create/', views.create_goal, name='create_goal'),
]