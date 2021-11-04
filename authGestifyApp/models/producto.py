from django.db import models
from django.db.models.fields.related import ForeignKey
from .user import User
from .proveedor import Proveedor 


categorias=(
    ('Des', 'Despensa'),
    ('Beb', 'Bebidas'),
    ('Mas', 'Para_Mascotas'),
    ('Beb', 'Para_Bebés'),
    ('AP',  'Aseo_Personal'),
    ('Lim', 'Limpieza'),
)

class Producto(models.Model):
    code = models.CharField('Code', max_length = 8 ,primary_key=True)
    user = models.ForeignKey(User, related_name='producto', on_delete=models.CASCADE)
    prov_name = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    p_name = models.CharField('Product_name', max_length=40)
    quantity = models.IntegerField()
    movement= models.CharField('entry/exit', max_length=10)
    price = models.CharField('Price', max_length = 15)
    category = models.CharField(max_length= 10)
    description = models.CharField('Description', max_length = 200)
    