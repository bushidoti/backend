from rest_framework import serializers
from .models import *


class AutoIncrementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrementProperty
        fields = '__all__'


class AirportEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportEquipment
        fields = '__all__'


class SafetyEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyEquipment
        fields = '__all__'


class AirportVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportVehicle
        fields = '__all__'


class OfficeVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeVehicle
        fields = '__all__'


class ElectronicFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicFurniture
        fields = '__all__'


class FacilityFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityFurniture
        fields = '__all__'


class DigitalFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalFurniture
        fields = '__all__'


class OfficeFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeFurniture
        fields = '__all__'


class IndustrialToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustrialTool
        fields = '__all__'


class NoneIndustrialToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoneIndustrialTool
        fields = '__all__'


class SupportItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportItem
        fields = '__all__'


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'


class AirportFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportFurniture
        fields = '__all__'


class RepairedDigitalFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedDigitalFurniture
        fields = '__all__'


class RepairedFacilityFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedFacilityFurniture
        fields = '__all__'


class RepairedOfficeFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedOfficeFurniture
        fields = '__all__'


class RepairedAirportFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedAirportFurniture
        fields = '__all__'


class RepairedElectronicFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedElectronicFurniture
        fields = '__all__'


class RepairedSafetyEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedSafetyEquipment
        fields = '__all__'


class RepairedAirportEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedAirportEquipment
        fields = '__all__'


class RepairedAirportVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedAirportVehicle
        fields = '__all__'


class RepairedOfficeVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedOfficeVehicle
        fields = '__all__'


class RepairedIndustrialToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairedIndustrialTool
        fields = '__all__'
