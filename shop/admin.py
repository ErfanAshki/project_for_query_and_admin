from django.contrib import admin
from django.db.models import Count

from .models import Product, Cart, CartItem, Category, Comment, Customer ,Order, OrderItem, Discount, Address


class InventoryFilter(admin.SimpleListFilter):
    title = 'Critical Inventory Status'
    parameter_name = 'inventory'
    LESS_THAN_3 = '<3'
    BETWEEN_3_AND_10 = '3<=10'
    GREATER_THAN_10 = '>10'

    def lookups(self, request, model_admin):
        return [
            (InventoryFilter.LESS_THAN_3, 'High'),
            (InventoryFilter.BETWEEN_3_AND_10, 'Medium'),
            (InventoryFilter.GREATER_THAN_10, 'Ok')
        ]

    def queryset(self, request, queryset):
        if self.value() == InventoryFilter.LESS_THAN_3:
            return queryset.filter(inventory__lt=3)
        elif self.value() == InventoryFilter.BETWEEN_3_AND_10:
            return queryset.filter(inventory__range=(3, 10))
        elif self.value() == InventoryFilter.GREATER_THAN_10:
            return queryset.filter(inventory__gt=10)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_title' , 'unit_price', 'inventory', 'inventory_status', 'datetime_created']
    ordering = ['id']
    list_per_page = 20    
    list_editable = ['unit_price', 'inventory']
    list_select_related = ['category']
    list_filter = [InventoryFilter, 'category']
    
    def inventory_status(self, product):
        if product.inventory < 10 :
            return 'LOW'
        elif product.inventory > 50 : 
            return 'HIGH'
        else:
            return 'MEDIUM'
        
    @admin.display(ordering='category__title')
    def category_title(self , product):
        return product.category.title
        
    
admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'datetime_created', 'number_of_items']
    ordering = ['id']
    list_per_page = 15    
    list_editable = ['status']
    list_filter = ['status']
    
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('items'). \
            annotate(items_count=Count('items'))
    
    @admin.display(ordering='items_count')
    def number_of_items(self, order):
        return order.items_count
    
    
admin.site.register(Order, OrderAdmin)


