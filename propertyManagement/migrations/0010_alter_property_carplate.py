# Generated by Django 4.2 on 2023-05-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyManagement', '0009_remove_person_topiccontract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='carPlate',
            field=models.CharField(max_length=2),
        ),
    ]