from django.urls import path
from application.views import register,login,home,logout_view,add_expense,add_income,delete_expense

urlpatterns = [
    path('home/',home,name='home'),

path('login/',login,name='login'),
path('',register,name='register'),
path('logout/',logout_view,name='logout'),

path('add-expense/',add_expense,name='add_expense'),
path('add-income/',add_income,name='add_income'),
path('delete-expense/<int:id>/',delete_expense,name='delete_expense'),
    ]