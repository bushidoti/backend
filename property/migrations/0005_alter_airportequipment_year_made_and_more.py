# Generated by Django 4.2 on 2023-06-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_airportequipment_airportfurniture_airportvehicle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airportequipment',
            name='year_made',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='airportfurniture',
            name='year_buy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='airportvehicle',
            name='year_made',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='digitalfurniture',
            name='year_buy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='electronicfurniture',
            name='year_buy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='facilityfurniture',
            name='year_buy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='industrialtool',
            name='year_buy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='noneindustrialtool',
            name='year_buy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='officefurniture',
            name='year_made',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='officevehicle',
            name='year_made',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='safetyequipment',
            name='year_made',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
