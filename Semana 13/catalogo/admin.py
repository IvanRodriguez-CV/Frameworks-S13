from django.contrib import admin

from .models import Categoria, Cliente, Producto, Rol, TipoPago


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion", "created_at", "updated_at")
    search_fields = ("nombre", "descripcion")


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "categoria", "precio", "stock")
    list_filter = ("categoria",)
    search_fields = ("nombre", "descripcion")


@admin.register(TipoPago)
class TipoPagoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "apellidos", "email", "telefono")
    search_fields = ("nombres", "apellidos", "email")


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)
