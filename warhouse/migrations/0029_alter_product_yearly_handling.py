# Generated by Django 4.2 on 2023-06-21 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhouse', '0028_product_yearly_handling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='yearly_handling',
            field=models.DateField(blank=True, null=True),
        ),
    ]