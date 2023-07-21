from .models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source="categoria_id.nombre")
    class Meta:
        model = Producto
        fields = '__all__'