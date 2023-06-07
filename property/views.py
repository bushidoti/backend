import django_filters
from rest_framework import viewsets
from .serializer import *
from .models import *


class AutoIncrementPropertyApi(viewsets.ModelViewSet):
    serializer_class = AutoIncrementSerializer
    queryset = AutoIncrementProperty.objects.all()
