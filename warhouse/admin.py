from django.contrib import admin
from .models import Product, AllProducts, AutoIncrement

admin.site.register(Product)
admin.site.register(AllProducts)
admin.site.register(AutoIncrement)
