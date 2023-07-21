#vistas y urls es lo que mas se usa
from django.urls import path
from . import views

app_name = "carro"

urlpatterns = [
    path('agregarProductoCarrito/<int:sku>/',views.Agregar_Producto, name="agregar"),
    path('eliminarDelCarrito/<int:sku>/',views.eliminar_Producto, name="eliminar"),
    path('restarDelCarrito/<int:sku>/',views.restar_Producto, name="restar"),
    path('limparCarrito/',views.Limpiar_Carro, name="limpiar")
]
