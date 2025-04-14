from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),  # Ruta para el panel de administración
    path("", include("sample_mflix.urls")),  # Incluye las rutas de la app sample_mflix
]