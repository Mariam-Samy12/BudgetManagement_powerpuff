from django.urls import path
from . import views

urlpatterns=[
  path ('',views.signup,name='signup'),
  path('loginv',views.loginv,name='login'),
    path('about/', views.about, name='about'),
    path('logoutv', views.logoutv, name='logoutv'),
]