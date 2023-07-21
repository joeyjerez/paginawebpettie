from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm #para formulario registro
from django.contrib.auth.models import User

#FORMULARIO DE CONTACTO
class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'
        
#FIN FORMULARIO CONTACTO

#FORMULARIO AGREGAR PRODUCTOS
class ProductoForm(forms.ModelForm):
    #VALIDACIONES AL MOMENTO DE AGREGAR UN PRODUCTO
    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=1500000)

    class Meta:
        model = Producto
        fields = '__all__'
        
        widgets = {
            "fecha_vencimiento":forms.SelectDateWidget()
        }


#Formulario Registro
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]