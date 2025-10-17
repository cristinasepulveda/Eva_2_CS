from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal, name="inicio"),
    path('detalle/<int:id>', views.detalle_producto, name="detalle"),
    path('categorias/', views.categorias, name="categorias"),
    path('categorias/<int:id>', views.categoria_detalle, name="categoria_detalle")
]
