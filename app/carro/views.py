from django.shortcuts import render

from app.models import Producto
from .carro import Carro

from django.shortcuts import redirect
# Create your views here.
  

def Agregar_Producto(request, sku):
    carro = Carro(request)
    producto = Producto.objects.get(sku = sku)

    carro.agregarProductoCarrito(producto=producto)

    return redirect('/productos')

def eliminar_Producto(request, sku):
    carro = Carro(request)
    producto = Producto.objects.get(sku = sku)

    carro.eliminarDelCarrito(producto=producto)

    return redirect("/productos")

def restar_Producto(request, sku):
    carro = Carro(request)
    producto = Producto.objects.get(sku = sku)

    carro.restarDelCarrito(producto=producto)

    return redirect("/productos")

def Limpiar_Carro(request):
    carro = Carro(request)
    carro.limparCarrito()
    return redirect("/productos")


