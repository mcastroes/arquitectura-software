from django.contrib import admin
from django.urls import path, include
from app_gestion_taller import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('gestion/', include('app_gestion_taller.urls')),
    path('acerca/', views.acerca_de, name='acerca'),
    path('contacto/', views.contacto, name='contacto'),
]
