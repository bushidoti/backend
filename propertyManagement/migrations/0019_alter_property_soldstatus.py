# Generated by Django 4.2 on 2023-06-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyManagement', '0018_alter_person_approvedprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='soldStatus',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
