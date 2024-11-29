from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_task/<str:pk>', views.update_task, name='update_task'),
    path('delete_task/<str:pk>', views.delete_task, name='delete_task'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]