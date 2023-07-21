from django.db import models

# Create your models here.


# Crear modelo, las clases van con primera letra en mayuscula

#Siempre que se hace un cambio en la clase (MODELO), se debe hacer juna migracion!!!OJO, en el caso de solo agregar formato no se hacen migraciones!
#Luego de haber realizado esto, se debe IR A REGISTRAR LOS MODELOS A admin.py

#INICIO CLASE CATEGORIA
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True) #autofiel deja como numerico y va agregando a la secuencia
    nombre = models.CharField(max_length=50, null=False)

    #Para darle formato a los items de la tabla que mostraremos en la admin de Django (formateo)
    def __str__(self):
        txt = "Nombre: {0} - {1}"
        return txt.format(self.nombre, self.categoria_id) #Esto se hace para cambiar el nombre en la base de datos 
#FIN CLASE CATEGORIA


#INICIO CLASE PRODUCTO
class Producto(models.Model):
    sku = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False) #para que no sea opcional se deja en false
    descripcion = models.CharField(max_length=150, null=False)
    stock = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True) #cambiar a true!
    categoria_id = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    

    #Para darle formato a los items de la tabla que mostraremos en la admin de Django (formateo)
    def __str__(self):
        txt = "N° {0} - Nombre: {1} - Stock {2} - Fecha: {3}" #Siempre las posiciones parten desde el 0
        return txt.format(self.sku,self.nombre,self.stock,self.fecha_ingreso)
#FIN CLASE PRODUCTO



opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]


#INICIO CLASE CONTACTO
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
#FIN CLASE CONTACTO