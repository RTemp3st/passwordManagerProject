from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='home-page'),
    path('registeration/', views.registeration, name='registeration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]