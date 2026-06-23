"""
URL configuration for proyectociudad project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('ordenamiento/', include('ordenamiento.urls')),
]
=======
    path('', include('ordenamiento.urls')),
]
>>>>>>> 1d0228d99bf39a117dbc4e2a6bf5261526b7ec2e
