from django.conf import settings
from django.db.models.query_utils import PathInfo
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authGestifyApp.models.user import User
from authGestifyApp.models.proveedor import Proveedor
from authGestifyApp.models.producto import Producto
from authGestifyApp.serializers.userSerializer import UserSerializer
from authGestifyApp.serializers.productoSerializer import ProductoSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):        

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        product = Producto.objects.get(code=self.kwargs["fk"])
        product = ProductoSerializer(product)

        return Response(product.data)

    def put(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        request.data["user"] = int(User.objects.get(id=self.kwargs["pk"]).id)
        request.data["code"] = self.kwargs["fk"]
        instance = Producto.objects.get(code=self.kwargs["fk"])
        if(instance.user.id != self.kwargs["pk"]):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        request.data["prov_name"] = Proveedor.objects.get(p_name=request.data.get("prov_name"))
        ProductoSerializer().update(instance,request.data)

        return Response(status=status.HTTP_201_CREATED)
    
    def delete(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        product = Producto.objects.get(code=self.kwargs["fk"])
        if(product.user.id != self.kwargs["pk"]):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        product.delete()
        return Response(status=status.HTTP_200_OK)