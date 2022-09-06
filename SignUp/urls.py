from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('sup',views.sup,name='signup_data'),
    path('login',views.login,name='login'),
    path('loginHandle',views.loginHandle,name='loginHandle'),
    path('logout',views.logout,name='logout'),
]