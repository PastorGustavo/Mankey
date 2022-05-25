from django.contrib import admin
from . import models
# Register your models here.


class ProdutoAdm(admin.ModelAdmin):

    model = models.Produto

    list_display = ['nome','preco']
    list_display_links = ['nome',]


admin.site.register(models.Produto, ProdutoAdm)