from django.contrib import admin
from .models import Product, AllProducts, AutoIncrement, PendingProducts

admin.site.register(Product)
admin.site.register(AllProducts)
admin.site.register(AutoIncrement)
admin.site.register(PendingProducts)
