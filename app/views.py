from django.shortcuts import render, redirect, get_object_or_404 #para modificar usamos redirect y 404
from .models import Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm #customcreationform es para el registro
from django.contrib import messages #para enviar mensajes
from django.core.paginator import Paginator #para mostrar los productos por paginas
from django.http import Http404#para mostrar error de pagina no encontrada
from django.contrib.auth import authenticate, login #para autenticar usuario
from django.contrib.auth.decorators import login_required, permission_required #Para que pida un permiso en concreto que debe tener el usuario.
from rest_framework import viewsets
from .serializers import ProductoSerializer
# Create your views here.

class ProductoViewset(viewsets.ModelViewSet): #Este viewset llama a todos los productos
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer #El serializador los convierte a JSON


#VISTA INICIO
def home(request):
    return render(request, 'app/home.html')
#FIN INICIO


#VISTA PRODUCTOS Y SU FUNCION
def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)

#FIN PRODUCTOS


#VISTA EQUIPO
#login_required SE USA PARA QUE UN USUARIO DEBA ESTAR LOGUEADO SI QUIERE ACCEDER A UNA VISTA EN ESPECÍFICO, EN EL CASO DE QUE QUIERA COMPRAR.
def equipo(request):
    return render(request, 'app/equipo.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')
#FIN EQUIPO


#VISTA CONTACTO Y SUS FUNCIONES
def contacto(request):
    data = {
        'form': ContactoForm()
    }


    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tu mensaje ha sido enviado")
            return redirect(to="home")
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)
#FIN CONTACTO


#VISTA AGREGAR PRODUCTO
@permission_required('app.add_producto') #El usuario debe tener permisos de agregar productos si quiere realizar esta accion , de lo contrario no podrá.
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

#FIN AGREGAR 

#VISTA LISTAR Y SU FUNCION
@permission_required('app.view_producto') #El usuario debe tener permisos de ver productos si quiere realizar esta accion , de lo contrario no podrá.
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1) #si no existe cierta pagina, que envie un 1 de vuelta

    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render(request, 'app/producto/listar.html', data)

#FIN LISTAR

#VISTA MODIFICAR
@permission_required('app.change_producto') #El usuario debe tener permisos de modificar productos si quiere realizar esta accion , de lo contrario no podrá.
def modificar_producto(request, sku):

    producto = get_object_or_404(Producto, sku=sku) #cual será el modelo y condicion, en este caso buscará el id que pongamos en la url

    data = {
        'form': ProductoForm(instance=producto) #la instancia será el producto que se busque en la base de datos
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES) 
        if formulario.is_valid():#SE VALIDA
            formulario.save()#SE GUARDA
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_productos")#EL USUARIO HACIA EL LISTADO
        data["form"] = formulario
        

    return render(request, 'app/producto/modificar.html', data)

#FIN MODIFICAR

#VISTA ELIMINAR
@permission_required('app.delete_producto') #El usuario debe tener permisos de eliminar productos si quiere realizar esta accion , de lo contrario no podrá.
def eliminar_producto(request, sku):
    producto = get_object_or_404(Producto, sku=sku)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_productos")

#FIN ELIMINAR

#REGISTRO DE USUARIOS
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])#ESTO DEVUELVE AL USUARIO AUTENTICADO.
            login(request, user)
            messages.success(request, "Te has registrado correctamente!")
            return redirect(to="home")
        data["form"] = formulario


    return render(request, 'registration/registro.html', data)

#FIN REGISTRO