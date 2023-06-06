import django_filters
from rest_framework import viewsets
from .serializer import *
from .models import *


class AutoIncrement101Api(viewsets.ModelViewSet):
    serializer_class = AutoIncrement101Serializer
    queryset = AutoIncrement101.objects.all()


class AutoIncrement102Api(viewsets.ModelViewSet):
    serializer_class = AutoIncrement102Serializer
    queryset = AutoIncrement102.objects.all()


class AutoIncrement103Api(viewsets.ModelViewSet):
    serializer_class = AutoIncrement103Serializer
    queryset = AutoIncrement103.objects.all()


class AutoIncrement104Api(viewsets.ModelViewSet):
    serializer_class = AutoIncrement104Serializer
    queryset = AutoIncrement104.objects.all()


class AutoIncrement105Api(viewsets.ModelViewSet):
    serializer_class = AutoIncrement105Serializer
    queryset = AutoIncrement105.objects.all()


class AutoIncrement106Api(viewsets.ModelViewSet):
    serializer_class = AutoIncrement106Serializer
    queryset = AutoIncrement106.objects.all()


class AutoIncrement107Api(viewsets.ModelViewSet):
    serializer_class = AutoIncrement107Serializer
    queryset = AutoIncrement107.objects.all()
