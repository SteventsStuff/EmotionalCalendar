from django.contrib.auth import views as dj_views
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('signout/', dj_views.LogoutView.as_view(), name='signout'),
]
