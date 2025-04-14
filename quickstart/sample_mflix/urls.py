from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la URL raíz
    path('create-client/', views.create_client, name='create_client'),  # Ruta para crear un cliente
]