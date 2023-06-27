# Generated by Django 4.2 on 2023-05-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='clearedDatePicker',
            new_name='clearedDate',
        ),
        migrations.AddField(
            model_name='document',
            name='doc_1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='doc_2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='doc_3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='doc_4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='doc_bail_1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='doc_bail_2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]