from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authGestifyApp.models.user import User
from authGestifyApp.models.producto import Producto
from authGestifyApp.serializers.userSerializer import UserSerializer
from authGestifyApp.serializers.productoSerializer import ProductoSerializer

class ProductView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):        

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        uid = self.kwargs["pk"]

        productQuerySet =  Producto.objects.all().filter(user=uid)
        serialized = ProductoSerializer(productQuerySet, many=True)

        return Response(serialized.data)

    def post(self, request, *args, **kwargs):
        uid = self.kwargs["pk"]
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        request.data["user"] = uid
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        content = {
            'user': str(request.user),
        }

        return Response(content,status=status.HTTP_201_CREATED)