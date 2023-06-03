from django.db import models


class Product(models.Model):
    code = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    scale = models.CharField(max_length=50, blank=True, null=True)
    inventory = models.CharField(max_length=50, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    input = models.BigIntegerField(blank=True, null=True)
    output = models.BigIntegerField(blank=True, null=True)
    left_stock = models.BigIntegerField(default=False, blank=True, null=True)
    document_type = models.CharField(max_length=50, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    recycle_status = models.CharField(max_length=50, blank=True, null=True)
    recycle_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=50, blank=True, null=True)


class AllProducts(models.Model):
    consumable = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    input = models.BigIntegerField(blank=True, null=True)
    output = models.BigIntegerField(blank=True, null=True)
    afterOperator = models.BigIntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    scale = models.CharField(max_length=50, blank=True, null=True)
    inventory_dst = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    buyer = models.CharField(max_length=50, blank=True, null=True)
    receiver = models.CharField(max_length=50, blank=True, null=True)
    document_type = models.CharField(max_length=50, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    factor = models.TextField(blank=True, null=True)
    checkBill = models.TextField(blank=True, null=True)
    amendment = models.TextField(blank=True, null=True)
    obsolete = models.BooleanField(blank=True, null=True)


class PendingProducts(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    input = models.BigIntegerField(blank=True, null=True)
    scale = models.CharField(max_length=50, blank=True, null=True)
    inventory_src = models.CharField(max_length=50, blank=True, null=True)
    inventory_dst = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    receiver = models.CharField(max_length=50, blank=True, null=True)
    document_type = models.CharField(max_length=50, blank=True, null=True)
    document_code = models.CharField(max_length=50, blank=True, null=True)
    factor = models.TextField(blank=True, null=True)
    checkBill = models.TextField(blank=True, null=True)
    amendment = models.TextField(blank=True, null=True)
    agree = models.BooleanField(blank=True, null=True)
    disagree = models.BooleanField(blank=True, null=True)


class AutoIncrement(models.Model):
    oghab101 = models.BigIntegerField(blank=True, null=True)
    oghab102 = models.BigIntegerField(blank=True, null=True)
    oghab103 = models.BigIntegerField(blank=True, null=True)
    oghab104 = models.BigIntegerField(blank=True, null=True)
    oghab105 = models.BigIntegerField(blank=True, null=True)
    oghab106 = models.BigIntegerField(blank=True, null=True)
    oghab107 = models.BigIntegerField(blank=True, null=True)
