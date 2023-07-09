from rest_framework import serializers
from .models import Product, AllProducts, AutoIncrement, Handling


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class AllProductsSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = AllProducts
        fields = '__all__'


class HandlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handling
        fields = '__all__'


class AutoIncrementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrement
        fields = '__all__'
