# Generated by Django 4.2 on 2023-05-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0018_alter_document_doc_2_alter_document_doc_3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='clearedStatus',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]