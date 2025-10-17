from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.
def principal(request):
    context = {}
    productos = Producto.objects.all()
    context['productos'] = productos
    return render(request,"base.html",context)


def categorias(request):
    context = {}
    categorias = Categoria.objects.all()
    context['categorias'] = categorias
    return render(request, 'categorias.html', context)

def detalle_producto(request,id):
    context = {}
    producto = Producto.objects.get(id=id)
    context['producto'] = producto
    return render(request, "detalles.html",context)

def categoria_detalle(request, id):
    categoria = Categoria.objects.get (id=id)
    productos = Producto.objects.filter(categoria=categoria)
    context = {
        'categoria': categoria,
        'productos': productos
    }
    return render(request, 'categoria_detalle.html', context)
