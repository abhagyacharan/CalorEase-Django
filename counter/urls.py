# counter urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('foodie/', views.home, name='home'),
]