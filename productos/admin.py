from django.contrib import admin
from .models import Producto
# Register your models here.


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "stock", "fecha_creacion")
    search_fields = ("nombre",)