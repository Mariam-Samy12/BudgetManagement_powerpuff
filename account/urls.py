from django.urls import path
from . import views

urlpatterns=[
  path ('',views.signup,name='signup'),
  path('login',views.login,name='login'),
   path('Home',views.home,name='Home'),
    path('about/', views.about, name='about'),
]