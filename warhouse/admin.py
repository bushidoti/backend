from django.contrib import admin
from .models import Product, AllProducts, AutoIncrement, Handling

admin.site.register(Product)
admin.site.register(AllProducts)
admin.site.register(AutoIncrement)
admin.site.register(Handling)
