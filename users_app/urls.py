from . import views
from django.urls import path


urlpatterns = [
    path('', views.login_user, name='login-user'),
    path('sign-up', views.register, name='register'),
    path('logout-user', views.logout_user, name='logout-user'),
     
]
