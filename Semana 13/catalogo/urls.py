from django.urls import path

from .views.categoria import (
    actualizar_categoria,
    agregar_categoria,
    eliminar_categoria,
    lista_categorias,
)
from .views.producto import (
    actualizar_producto,
    agregar_producto,
    eliminar_producto,
    lista_productos,
)


urlpatterns = [
    path("", lista_categorias, name="inicio"),
    path("categoria/", lista_categorias, name="list_categorias"),
    path("categoria/add/", agregar_categoria, name="add_categoria"),
    path(
        "categoria/<int:id>/update/",
        actualizar_categoria,
        name="update_categoria",
    ),
    path(
        "categoria/<int:id>/delete/",
        eliminar_categoria,
        name="delete_categoria",
    ),
    path("productos/", lista_productos, name="list_productos"),
    path("productos/add/", agregar_producto, name="add_producto"),
    path(
        "productos/<int:id>/update/",
        actualizar_producto,
        name="update_producto",
    ),
    path(
        "productos/<int:id>/delete/",
        eliminar_producto,
        name="delete_producto",
    ),
]
