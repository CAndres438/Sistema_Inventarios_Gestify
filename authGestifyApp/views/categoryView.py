from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

class CategoryView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        categories =(
            {"cod" :'Des', "name": "Despensa"},
            {"cod" :'Beb', "name": "Bebidas"},
            {"cod" :'Mas', "name": "Para_Mascotas"},
            {"cod" :'Beb', "name": "Para_Bebés"},
            {"cod" :'AP',  "name": "Aseo_Personal"},
            {"cod" :'Lim', "name": "Limpieza"},
        )
        
        return Response(categories,status=status.HTTP_200_OK)