import django_filters
from rest_framework import viewsets
from .serializer import ProductSerializer, AllProductsSerializer
from .models import Product, AllProducts


class ProductApi(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'category', 'date',
                        'inventory', 'recycle_status', 'operator']


class AllProductstApi(viewsets.ModelViewSet):
    serializer_class = AllProductsSerializer
    queryset = AllProducts.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'date', 'consumable']
