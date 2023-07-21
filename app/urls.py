from django.urls import path, include
from .views import home, productos, equipo, nosotros, contacto, agregar_producto, listar_productos, modificar_producto, eliminar_producto, registro, ProductoViewset
from rest_framework import routers


router = routers.DefaultRouter() #Crear urls necesarias para nuestra api
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('equipo/', equipo, name="equipo"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<sku>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<sku>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls))
]