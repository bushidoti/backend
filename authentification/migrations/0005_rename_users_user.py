# Generated by Django 4.2 on 2023-05-07 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0004_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]