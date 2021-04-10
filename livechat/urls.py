from django.urls import path
from django.urls.conf import include
from . import views

# app_name = 'livechat'

urlpatterns = [
    path('',views.index,name='chat'),
    path('chan/',views.index,name='chat_index'),
    path('<str:room_name>/', views.room, name='room'),
]