# Generated by Django 4.2 on 2023-06-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhouse', '0011_remove_allproducts_beforeoperator'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproducts',
            name='amendment',
            field=models.TextField(blank=True, null=True),
        ),
    ]