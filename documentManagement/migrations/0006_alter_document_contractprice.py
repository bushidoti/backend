# Generated by Django 4.2 on 2023-05-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0005_document_clearedstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='contractPrice',
            field=models.CharField(max_length=50),
        ),
    ]
