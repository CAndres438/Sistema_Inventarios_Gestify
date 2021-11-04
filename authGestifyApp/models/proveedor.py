from django.db import models
from django.db.models.fields.related import ForeignKey
from .user import User

class Proveedor(models.Model):    
    p_name = models.CharField('Suplier', max_length=30, primary_key=True)
    p_telephone = models.CharField('Telephone', max_length = 10)
    p_email = models.CharField('Email', max_length = 100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
