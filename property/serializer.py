from rest_framework import serializers
from .models import *


class AutoIncrementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrementProperty
        fields = '__all__'
