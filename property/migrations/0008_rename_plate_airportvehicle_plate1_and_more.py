# Generated by Django 4.2 on 2023-06-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_rename_owner_safetyequipment_use_for'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airportvehicle',
            old_name='plate',
            new_name='plate1',
        ),
        migrations.RenameField(
            model_name='officevehicle',
            old_name='plate',
            new_name='plate1',
        ),
        migrations.AddField(
            model_name='airportvehicle',
            name='plate2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='airportvehicle',
            name='plate3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='airportvehicle',
            name='plate4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='officevehicle',
            name='plate2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='officevehicle',
            name='plate3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='officevehicle',
            name='plate4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
