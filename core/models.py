from operator import mod
from django.db import models

class Produto(models.Model):
    link = models.CharField(max_length=9999)
    img = models.ImageField(upload_to='media/%Y/%m/%d')
    nome = models.CharField(max_length=300)
    preco = models.IntegerField()

    pais =  models.CharField(
        max_length=2,
        choices=(
            ('Br','Brasil'),
            ('ES','Internacional')
            )
        )