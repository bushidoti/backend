# Generated by Django 4.2 on 2023-05-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0015_alter_document_doc_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
