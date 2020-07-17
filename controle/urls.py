from django.urls import path

from.views import index, produto, compra, estoque, comprasrealizadas, cadastro

urlpatterns = [
    path('', index, name='index'),
    path('produto/', produto, name='produto'),
    path('compra/', compra, name='compra'),
    path('estoque/', estoque, name='estoque'),
    path('comprasrealizadas/', comprasrealizadas, name='comprasrealizadas'),
    path('cadastro/', cadastro, name='cadastro'),
]

