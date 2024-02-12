from rest_framework import serializers
from .models import Cliente, Produto, GrupoProduto, Venda, Vendedor, ItemVenda

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
