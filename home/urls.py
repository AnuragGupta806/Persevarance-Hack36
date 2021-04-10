from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_user,name='login'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('assignment/',views.assign,name='assignment'),
]