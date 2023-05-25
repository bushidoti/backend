from rest_framework import serializers
from .models import Product, AllProducts


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AllProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllProducts
        fields = '__all__'
