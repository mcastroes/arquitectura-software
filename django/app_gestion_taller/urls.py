from django.urls import path
from . import views
from .views import (
    lista_clientes,
    detalle_cliente,
    registrar_cliente,
    registrar_coche,
    buscar_coche_por_matricula,
    buscar_coches_de_cliente,
    registrar_servicio,
    buscar_servicios_de_coche,
    nuevo_cliente,
    nuevo_coche,
    nuevo_servicio,
    asignar_servicio
)

urlpatterns = [
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('clientes/registrar/', registrar_cliente, name='registrar_cliente'),
    path('coches/registrar/', registrar_coche, name='registrar_coche'),
    path('coches/matricula/<str:matricula>/', buscar_coche_por_matricula, name='buscar_coche_por_matricula'),
    path('clientes/<int:cliente_id>/coches/', buscar_coches_de_cliente, name='buscar_coches_de_cliente'),
    path('servicios/registrar/', registrar_servicio, name='registrar_servicio'),
    path('coches/<int:coche_id>/servicios/', buscar_servicios_de_coche, name='buscar_servicios_de_coche'),
    path('clientes/nuevo/', nuevo_cliente, name='nuevo_cliente'), 
    path('coches/nuevo/', nuevo_coche, name='nuevo_coche'),
    path('servicios/nuevo/', nuevo_servicio, name='nuevo_servicio'),
    path('asignar_servicio/', asignar_servicio, name='asignar_servicio'),
]