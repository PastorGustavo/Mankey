from . import models
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView

# Create your views here.
class Index(View):
    
    def get(self,*args,**kwargs):

        return render(self.request,'core/index.html')


class Produtos(ListView):
    template_name = 'core/produtos.html'
    model = models.Produto
    context_object_name = 'produtos'