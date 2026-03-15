from django.urls import path
from application.views import register,login

urlpatterns = [
    path('',register,name='register'),
    path('login/',login,name='login'),
]