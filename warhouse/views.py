import django_filters
from rest_framework import viewsets
from .serializer import ProductSerializer, AllProductsSerializer, AutoIncrementSerializer, PendingProductsSerializer
from .models import Product, AllProducts, AutoIncrement, PendingProducts


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
    filterset_fields = ['id', 'date', 'consumable', 'document_code', 'document_type']


class PendingProductsApi(viewsets.ModelViewSet):
    serializer_class = PendingProductsSerializer
    queryset = PendingProducts.objects.all()


class AutoIncrementApi(viewsets.ModelViewSet):
    serializer_class = AutoIncrementSerializer
    queryset = AutoIncrement.objects.all()
