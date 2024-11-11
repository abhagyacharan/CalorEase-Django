# classify urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_page, name='upload_page'),
    path('predict/', views.predict_image, name='predict_image'),
    # path('debug/', views.debug_model, name='debug_model'),
]
