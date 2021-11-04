from authGestifyApp.models.producto import Producto
from django.db.models import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from authGestifyApp.models.proveedor import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor 
        fields = ['p_name', 'p_telephone', 'p_email','user']
        
    def create(self, validated_data):
        providerInstance = Proveedor.objects.create(**validated_data)
        return providerInstance

    def update(self, instance, validated_data):
        instance.p_name = validated_data.get("p_name", instance.p_name)
        instance.p_telephone = validated_data.get("p_telephone", instance.p_telephone)
        instance.p_email = validated_data.get("p_email", instance.p_email)
        instance.user = validated_data.get("user", instance.user)
        instance.save()
        return instance

    def to_representation(self, obj):
        provider = Proveedor.objects.get(p_name=obj.p_name)
        return {
            'p_name': provider.p_name,
            'p_telephone': provider.p_telephone,
            'p_email': provider.p_email,
            'user': provider.user.id,
        }
