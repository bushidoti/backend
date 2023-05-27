from rest_framework import serializers
from .models import Product, AllProducts, AutoIncrement


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AllProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllProducts
        fields = '__all__'


class AutoIncrementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrement
        fields = '__all__'
