from rest_framework import serializers
from authGestifyApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email']
        
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def update(self, instance, validated_data):
        print(instance)
        instance.id = instance.id
        instance.username = validated_data.get("username", instance.username)
        instance.password = validated_data.get("password", instance.password)
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email,
                }