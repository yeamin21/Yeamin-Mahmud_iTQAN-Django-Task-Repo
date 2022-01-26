
from importlib.resources import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView
from django.urls import path

app_name = 'users'
urlpatterns = [     
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('register/',UserRegisterView.as_view(), name='register'),
]
