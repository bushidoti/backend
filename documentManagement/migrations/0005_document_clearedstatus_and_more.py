# Generated by Django 4.2 on 2023-05-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0004_rename_cleareddatepicker_document_cleareddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='clearedStatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='document',
            name='receivedDocument',
            field=models.BooleanField(default=False),
        ),
    ]