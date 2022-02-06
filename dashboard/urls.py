from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('', views.IndexView.as_view(), name='index'),
]