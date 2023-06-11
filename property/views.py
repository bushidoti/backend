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
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'install_location', 'model', 'year_made', 'owner']


class SafetyEquipmentApi(viewsets.ModelViewSet):
    serializer_class = SafetyEquipmentSerializer
    queryset = SafetyEquipment.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'install_location', 'use_for']


class AirportVehicleApi(viewsets.ModelViewSet):
    serializer_class = AirportVehicleSerializer
    queryset = AirportVehicle.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'year_made', 'model', 'chassis', 'motor', 'plate1', 'plate2', 'plate3',
                        'plate4', 'owner']


class OfficeVehicleApi(viewsets.ModelViewSet):
    serializer_class = OfficeVehicleSerializer
    queryset = OfficeVehicle.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'year_made', 'model', 'chassis', 'motor', 'plate1', 'plate2', 'plate3',
                        'plate4', 'owner']


class AirportFurnitureApi(viewsets.ModelViewSet):
    serializer_class = AirportFurnitureSerializer
    queryset = AirportFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'install_location']


class FacilityFurnitureApi(viewsets.ModelViewSet):
    serializer_class = FacilityFurnitureSerializer
    queryset = FacilityFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'install_location', 'model', 'user']


class DigitalFurnitureApi(viewsets.ModelViewSet):
    serializer_class = DigitalFurnitureSerializer
    queryset = DigitalFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'install_location', 'model', 'user']


class OfficeFurnitureApi(viewsets.ModelViewSet):
    serializer_class = OfficeFurnitureSerializer
    queryset = OfficeFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'using_location', 'user', 'year_made']


class ElectronicFurnitureApi(viewsets.ModelViewSet):
    serializer_class = ElectronicFurnitureSerializer
    queryset = ElectronicFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'install_location', 'model', 'year_buy', 'user']


class NoneIndustrialToolApi(viewsets.ModelViewSet):
    serializer_class = NoneIndustrialToolSerializer
    queryset = NoneIndustrialTool.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'user', 'using_location']


class IndustrialToolApi(viewsets.ModelViewSet):
    serializer_class = IndustrialToolSerializer
    queryset = IndustrialTool.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'user', 'using_location', 'model']


class BenefitApi(viewsets.ModelViewSet):
    serializer_class = BenefitSerializer
    queryset = Benefit.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'number_type', 'number', 'using_location']


class SupportItemApi(viewsets.ModelViewSet):
    serializer_class = SupportItemSerializer
    queryset = SupportItem.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'using_location', 'model', 'type_item']


class RepairedDigitalFurnitureApi(viewsets.ModelViewSet):
    serializer_class = RepairedDigitalFurnitureSerializer
    queryset = RepairedDigitalFurniture.objects.all()


class RepairedFacilityFurnitureApi(viewsets.ModelViewSet):
    serializer_class = RepairedFacilityFurnitureSerializer
    queryset = RepairedFacilityFurniture.objects.all()


class RepairedOfficeFurnitureApi(viewsets.ModelViewSet):
    serializer_class = RepairedOfficeFurnitureSerializer
    queryset = RepairedOfficeFurniture.objects.all()


class RepairedAirportFurnitureApi(viewsets.ModelViewSet):
    serializer_class = RepairedAirportFurnitureSerializer
    queryset = RepairedAirportFurniture.objects.all()


class RepairedElectronicFurnitureApi(viewsets.ModelViewSet):
    serializer_class = RepairedElectronicFurnitureSerializer
    queryset = RepairedElectronicFurniture.objects.all()


class RepairedSafetyEquipmentApi(viewsets.ModelViewSet):
    serializer_class = RepairedSafetyEquipmentSerializer
    queryset = RepairedSafetyEquipment.objects.all()


class RepairedAirportEquipmentApi(viewsets.ModelViewSet):
    serializer_class = RepairedAirportEquipmentSerializer
    queryset = RepairedAirportEquipment.objects.all()


class RepairedAirportVehicleApi(viewsets.ModelViewSet):
    serializer_class = RepairedAirportVehicleSerializer
    queryset = RepairedAirportVehicle.objects.all()


class RepairedOfficeVehicleApi(viewsets.ModelViewSet):
    serializer_class = RepairedOfficeVehicleSerializer
    queryset = RepairedOfficeVehicle.objects.all()


class RepairedIndustrialToolApi(viewsets.ModelViewSet):
    serializer_class = RepairedIndustrialToolSerializer
    queryset = RepairedIndustrialTool.objects.all()
