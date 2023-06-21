# Generated by Django 4.2 on 2023-06-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_alter_airportequipment_sign_received_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airportequipment',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='airportequipment',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='airportequipment',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='airportfurniture',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='airportfurniture',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='airportfurniture',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='airportvehicle',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='airportvehicle',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='airportvehicle',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='benefit',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='benefit',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='benefit',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='digitalfurniture',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='digitalfurniture',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='digitalfurniture',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='electronicfurniture',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electronicfurniture',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='electronicfurniture',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='facilityfurniture',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilityfurniture',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='facilityfurniture',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='industrialtool',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='industrialtool',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='industrialtool',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='noneindustrialtool',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='noneindustrialtool',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='noneindustrialtool',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='officefurniture',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='officefurniture',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='officefurniture',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='officevehicle',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='officevehicle',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='officevehicle',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='safetyequipment',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='safetyequipment',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='safetyequipment',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='supportitem',
            name='last_handling_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supportitem',
            name='last_handling_result',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='supportitem',
            name='yearly_handling',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
