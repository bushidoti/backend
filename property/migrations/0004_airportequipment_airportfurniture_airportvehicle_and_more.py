# Generated by Django 4.2 on 2023-06-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_rename_autoincrement101_autoincrementproperty'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirportEquipment',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year_made', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('install_location', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AirportFurniture',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year_buy', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('install_location', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AirportVehicle',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year_made', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('install_location', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('plate', models.CharField(blank=True, max_length=50, null=True)),
                ('motor', models.CharField(blank=True, max_length=50, null=True)),
                ('chassis', models.CharField(blank=True, max_length=50, null=True)),
                ('kilometer', models.BigIntegerField(blank=True, null=True)),
                ('year_changed', models.IntegerField(blank=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('number_type', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('using_location', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DigitalFurniture',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_feature', models.CharField(blank=True, max_length=50, null=True)),
                ('cpu', models.CharField(blank=True, max_length=50, null=True)),
                ('motherboard', models.CharField(blank=True, max_length=50, null=True)),
                ('ram', models.CharField(blank=True, max_length=50, null=True)),
                ('power', models.CharField(blank=True, max_length=50, null=True)),
                ('hdd', models.CharField(blank=True, max_length=50, null=True)),
                ('case', models.CharField(blank=True, max_length=50, null=True)),
                ('year_buy', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('install_location', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('type_furniture', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElectronicFurniture',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year_buy', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('install_location', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacilityFurniture',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year_buy', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('install_location', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndustrialTool',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year_buy', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('using_location', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoneIndustrialTool',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('year_buy', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('using_location', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeFurniture',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('year_made', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('using_location', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeVehicle',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year_made', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('install_location', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
                ('plate', models.CharField(blank=True, max_length=50, null=True)),
                ('motor', models.CharField(blank=True, max_length=50, null=True)),
                ('chassis', models.CharField(blank=True, max_length=50, null=True)),
                ('kilometer', models.BigIntegerField(blank=True, null=True)),
                ('year_changed', models.IntegerField(blank=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SafetyEquipment',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year_made', models.IntegerField(blank=True, max_length=4, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('install_location', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('repaired_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupportItem',
            fields=[
                ('code', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('type_item', models.CharField(blank=True, max_length=50, null=True)),
                ('inventory', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('using_location', models.CharField(blank=True, max_length=50, null=True)),
                ('type_register', models.CharField(blank=True, max_length=50, null=True)),
                ('repaired_status', models.BooleanField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]