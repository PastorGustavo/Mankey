from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [

path('', views.Index.as_view(), name='index'),
path('produtos/', views.Produtos.as_view(), name='produtos'),
path('produtos/<str:local>', views.Produtos.as_view(), name='produtos')

]