from . import models
from django.shortcuts import redirect, render
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


    def get_termo(self):
        return self.kwargs.get('local')

    def get_queryset(self):
        
        """Aqui vamos filtrar as camisetas"""
        
        qs = super().get_queryset()

        # Pegando o termo
        term = self.get_termo()
        
        if term in ('br','es','all'):
            qs = qs.filter(pais__iexact=term)
        return qs

        