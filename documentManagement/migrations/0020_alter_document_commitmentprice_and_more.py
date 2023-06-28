# Generated by Django 4.2 on 2023-06-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0019_alter_document_clearedstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='commitmentPrice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='contractNumber',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='contractPrice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='dateContract',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='durationContract',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='firstBail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='firstBail2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='goodPrice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='prePaidPrice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='secondBail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='secondBail2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='topicContract',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='typeBail1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='typeBail2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='typeContract',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]