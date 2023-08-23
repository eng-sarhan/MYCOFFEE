from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','description','price','photo','is_active','publish_date')


admin.site.register(Product, ProductAdmin)
