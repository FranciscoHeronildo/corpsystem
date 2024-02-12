from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Produto, GrupoProduto, Venda, Vendedor, ItemVenda
from .serializers import ClienteSerializer, ProdutoSerializer, GrupoProdutoSerializer, VendaSerializer, VendedorSerializer, ItemVendaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
