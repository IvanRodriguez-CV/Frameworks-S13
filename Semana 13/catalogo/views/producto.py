from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from ..forms.producto_form import ProductoForm
from ..models.producto import Producto


def lista_productos(request):
    productos = Producto.objects.all()
    paginador = Paginator(productos, 10)
    pagina = request.GET.get("page")
    productos_paginados = paginador.get_page(pagina)
    return render(
        request,
        "producto/lista.html",
        {"productos": productos_paginados},
    )


def add_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_producto")
    else:
        form = ProductoForm()

    return render(request, "producto/add.html", {"form": form})


def update_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)

    if request.method == "POST":
        nombre_imagen_anterior = producto.imagen.name
        almacenamiento_imagen = producto.imagen.storage
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto_guardado = form.update(producto)
            nombre_imagen_nueva = producto_guardado.imagen.name
            if (
                nombre_imagen_anterior
                and nombre_imagen_nueva != nombre_imagen_anterior
            ):
                almacenamiento_imagen.delete(nombre_imagen_anterior)
            return redirect("list_producto")
    else:
        form = ProductoForm(
            initial={
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "precio_compra": producto.precio_compra,
                "precio_venta": producto.precio_venta,
                "stock": producto.stock,
                "categoria": producto.categoria,
                "imagen": producto.imagen,
            }
        )

    return render(
        request,
        "producto/update.html",
        {"form": form, "producto": producto},
    )


def delete_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if producto.imagen:
        producto.imagen.storage.delete(producto.imagen.name)
    producto.delete()
    return redirect("list_producto")
