from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from django.core import serializers as coreSerializers
from authGestifyApp.models.producto import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto 
        fields = ['code', 'user', 'prov_name', 'p_name', 'quantity','movement','price','category','description']

    def create(self, validated_data):
        productInstance = Producto.objects.create(**validated_data)
        return productInstance

    def update(self, instance, validated_data):
        print(instance)
        instance.code = instance.code
        instance.user = validated_data.get("user.id", instance.user)
        instance.prov_name = validated_data.get("prov_name", instance.prov_name)
        instance.p_name = validated_data.get("p_name", instance.p_name)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.movement = validated_data.get("movement", instance.movement)
        instance.price = validated_data.get("price", instance.price)
        instance.category = validated_data.get("category", instance.category)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

    def to_representation(self, obj):
        product = Producto.objects.get(code=obj.code)
        return {
            'code': product.code,
            'p_name': product.p_name,
            'description': product.description,
            'quantity': product.quantity,
            'category': product.category,
            'price': product.price,
            'prov_name': product.prov_name.p_name,
        }
