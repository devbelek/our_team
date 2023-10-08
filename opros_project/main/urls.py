from django.urls import path
from . import views

urlpatterns = [
    path('home', views.view_page, name='home'),
    path('', views.login_page, name='login'),
    path('register/', views.signup_page, name='signup'),
    path('chat', views.home, name='home_chat'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]