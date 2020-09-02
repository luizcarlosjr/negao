from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.listaCliente, name="lista-Cliente"),
    path('Cliente/<int:id>', views.clienteView, name="Cliente-View"),
    path('novocliente/', views.novocliente, name="novo-Cliente"),
    path('edit/<int:id>', views.editcliente, name="edit-cliente"),
    path('delete/<int:id>', views.deletecliente, name="delete-cliente"),
    path('seunome/<str:name>', views.seunome, name="seu-nome"),   
]


