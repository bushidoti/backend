import django_filters
from rest_framework import viewsets
from .serializer import *
from .models import *


class AutoIncrementPropertyApi(viewsets.ModelViewSet):
    serializer_class = AutoIncrementSerializer
    queryset = AutoIncrementProperty.objects.all()


class AirportEquipmentApi(viewsets.ModelViewSet):
    serializer_class = AirportEquipmentSerializer
    queryset = AirportEquipment.objects.all()


class SafetyEquipmentApi(viewsets.ModelViewSet):
    serializer_class = SafetyEquipmentSerializer
    queryset = SafetyEquipment.objects.all()


class AirportVehicleApi(viewsets.ModelViewSet):
    serializer_class = AirportVehicleSerializer
    queryset = AirportVehicle.objects.all()


class OfficeVehicleApi(viewsets.ModelViewSet):
    serializer_class = OfficeVehicleSerializer
    queryset = OfficeVehicle.objects.all()


class AirportFurnitureApi(viewsets.ModelViewSet):
    serializer_class = AirportFurnitureSerializer
    queryset = AirportFurniture.objects.all()


class FacilityFurnitureApi(viewsets.ModelViewSet):
    serializer_class = FacilityFurnitureSerializer
    queryset = FacilityFurniture.objects.all()


class DigitalFurnitureApi(viewsets.ModelViewSet):
    serializer_class = DigitalFurnitureSerializer
    queryset = DigitalFurniture.objects.all()


class OfficeFurnitureApi(viewsets.ModelViewSet):
    serializer_class = OfficeFurnitureSerializer
    queryset = OfficeFurniture.objects.all()


class ElectronicFurnitureApi(viewsets.ModelViewSet):
    serializer_class = ElectronicFurnitureSerializer
    queryset = ElectronicFurniture.objects.all()


class NoneIndustrialToolApi(viewsets.ModelViewSet):
    serializer_class = NoneIndustrialToolSerializer
    queryset = NoneIndustrialTool.objects.all()


class IndustrialToolApi(viewsets.ModelViewSet):
    serializer_class = IndustrialToolSerializer
    queryset = IndustrialTool.objects.all()


class BenefitApi(viewsets.ModelViewSet):
    serializer_class = BenefitSerializer
    queryset = Benefit.objects.all()


class SupportItemApi(viewsets.ModelViewSet):
    serializer_class = SupportItemSerializer
    queryset = SupportItem.objects.all()
