from django.contrib import admin

#Traemos los modelos de models.py
from .models import Categoria, Producto, Contacto


#clase para crear y ordenar columnas en el administrador de django
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "precio", "stock"]
    list_editable = ["precio", "stock"]
    search_fields = ["nombre"]
    list_filter = ["categoria_id"]
    list_per_page = 5


# Aqui los registramos

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)