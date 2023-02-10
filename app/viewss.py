from cart.models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets
from django.views import generic
from rest_framework import permissions


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class Error404View(generic.TemplateView):
    template_name = '404.html'
