from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, default='')


class Produto(models.Model):
    nome = models.CharField(max_length=100, default='')


class GrupoProduto(models.Model):
    nome = models.CharField(max_length=100, default='')

class Vendedor(models.Model):
    nome = models.CharField(max_length=100, default='')
    
class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    