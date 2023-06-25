# Generated by Django 4.2 on 2023-06-21 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warhouse', '0026_remove_allproducts_count_product_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Handling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhouse.product')),
            ],
        ),
    ]