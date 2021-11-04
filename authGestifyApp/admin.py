from django.contrib import admin
from .models.user import User
from .models.producto import Producto
from .models.proveedor import Proveedor



admin.site.register(User)
admin.site.register(Producto)
admin.site.register(Proveedor)
