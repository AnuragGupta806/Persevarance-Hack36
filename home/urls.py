from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_user,name='login'),
]