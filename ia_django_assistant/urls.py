"""
URL configuration for ia_django_assistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Vista simple para la raíz "/"
def home_view(request):
    return JsonResponse({
        "message": "Bienvenido a la API de ia_django_assistant",
        "endpoints_disponibles": ["/admin/", "/api/"]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chat.urls')),
    path('', home_view),  # Agregamos la ruta raíz
]
