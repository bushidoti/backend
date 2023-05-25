from django.db import models


class Product(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    number_in_out = models.BigIntegerField(blank=True, null=True)
    scale = models.CharField(max_length=50, blank=True, null=True)
    consumable = models.CharField(max_length=50, blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    left_stock = models.BigIntegerField(default=False, blank=True, null=True)
    document_type = models.CharField(max_length=50, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True, unique=True)
    recycle_status = models.CharField(max_length=50, blank=True, null=True)
    recycle_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)


class AllProducts(models.Model):
    consumable = models.CharField(max_length=50, blank=True, null=True)
    input = models.BigIntegerField(blank=True, null=True)
    output = models.BigIntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    scale = models.CharField(max_length=50, blank=True, null=True)
    inventory_dst = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    buyer = models.CharField(max_length=50, blank=True, null=True)
    receiver = models.CharField(max_length=50, blank=True, null=True)
    document_type = models.CharField(max_length=50, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
