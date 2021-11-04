from django.conf import settings
from django.db.models.query_utils import PathInfo
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authGestifyApp.models.user import User
from authGestifyApp.models.proveedor import Proveedor
from authGestifyApp.serializers.userSerializer import UserSerializer
from authGestifyApp.serializers.proveedorSerializer import ProveedorSerializer

class ProviderDetailView(generics.RetrieveAPIView):
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
        
        provider = Proveedor.objects.get(p_name=self.kwargs["fk"])
        if(provider.user.id != self.kwargs["pk"]):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        provider = ProveedorSerializer(provider)
        return Response(provider.data,status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        provider = Proveedor.objects.get(p_name=self.kwargs["fk"])
        if(provider.user.id != self.kwargs["pk"]):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        request.data["user"] = User.objects.get(id = self.kwargs["pk"])
        request.data["p_name"] = self.kwargs["fk"]
        ProveedorSerializer().update(provider,request.data)
        
        return Response({"info": "Change Updated"}, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        provider = Proveedor.objects.get(p_name=self.kwargs["fk"])
        if(provider.user.id != self.kwargs["pk"]):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        provider.delete()
        return Response(status=status.HTTP_200_OK)