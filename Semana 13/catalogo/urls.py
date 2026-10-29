from django.urls import path

from .views.categoria import (
    add_categoria,
    delete_categoria,
    lista_categorias,
    update_categoria,
)
from .views.producto import (
    add_producto,
    delete_producto,
    lista_productos,
    update_producto,
)


urlpatterns = [
    path("categoria/", lista_categorias, name="list_categoria"),
    path("categoria/agregar/", add_categoria, name="add_categoria"),
    path(
        "categoria/actualizar/<int:id>/",
        update_categoria,
        name="update_categoria",
    ),
    path(
        "categoria/eliminar/<int:id>/",
        delete_categoria,
        name="delete_categoria",
    ),
    path("producto/", lista_productos, name="list_producto"),
    path("producto/agregar/", add_producto, name="add_producto"),
    path(
        "producto/actualizar/<int:id>/",
        update_producto,
        name="update_producto",
    ),
    path(
        "producto/eliminar/<int:id>/",
        delete_producto,
        name="delete_producto",
    ),
]
