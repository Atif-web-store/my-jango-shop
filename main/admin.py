from django.contrib import admin
from .models import Product

# Product admin class
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description')  # admin list me columns
    search_fields = ('name', 'description')               # search box