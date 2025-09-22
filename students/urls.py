# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),      # default page → login
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]