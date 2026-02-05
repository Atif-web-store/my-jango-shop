from django.contrib import admin
from .models import Product, Order, Contact

# 1. Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category') # Columns jo list mein dikhenge
    list_filter = ('category',)                        # Side bar mein filter
    search_fields = ('name', 'description')            # Search box
    ordering = ('id',)

# 2. Order Admin (Tracking ke liye zaroori)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'status', 'is_paid', 'created_at') # Payment aur status dikhayega
    list_filter = ('status', 'is_paid', 'created_at')                          # Filter status ke hisab se
    search_fields = ('tracking_number', 'phone', 'address')                    # Tracking number se search
    list_editable = ('status', 'is_paid')                                      # List se hi status change karne ke liye
    ordering = ('-created_at',)                                                # Naya order sabse upar

# 3. Contact Admin (Customers ke message dekhne ke liye)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',) # Isko aap edit nahi kar sakte