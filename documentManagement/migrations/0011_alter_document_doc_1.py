# Generated by Django 4.2 on 2023-05-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0010_alter_document_type_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_1',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
