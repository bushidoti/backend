# Generated by Django 4.2 on 2023-05-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyManagement', '0013_remove_property_solddatepicker_property_solddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='type_form',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
