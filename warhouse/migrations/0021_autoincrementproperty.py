# Generated by Django 4.2 on 2023-06-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhouse', '0020_delete_pendingproducts_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoIncrementProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oghab101', models.BigIntegerField(blank=True, null=True)),
                ('oghab102', models.BigIntegerField(blank=True, null=True)),
                ('oghab103', models.BigIntegerField(blank=True, null=True)),
                ('oghab104', models.BigIntegerField(blank=True, null=True)),
                ('oghab105', models.BigIntegerField(blank=True, null=True)),
                ('oghab106', models.BigIntegerField(blank=True, null=True)),
                ('oghab107', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
    ]
