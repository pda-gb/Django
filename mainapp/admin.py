from django.contrib import admin
from .models import Product, ProductCategory, ProductType

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductType)