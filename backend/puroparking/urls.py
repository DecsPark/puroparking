"""
URL configuration for puroparking project.

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
from apps.usuario.views import *
from apps.facturacion.views import *
from apps.hora_parqueo.views import *
from apps.rol.views import *
from apps.vehiculo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('facturacion/', facturacionViewset.as_view(template_name='facturacion/facturacion.html')),
    path('hora_parqueo/', hora_parqueoViewset.as_view(template_name='hora_parqueo/hora_parqueo.html')),
    path('rol/', rolViewset.as_view(template_name='rol/rol.html')),
    path('vehiculo/', vehiculoViewset.as_view(template_name='vehiculo/vehiculo.html')),
    path('usuario/', usuarioViewset.as_view(template_name='usuario/usuario.html')),
    

]
