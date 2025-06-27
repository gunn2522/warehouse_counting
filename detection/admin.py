from django.contrib import admin
from .models import Product, FlowLog

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock')
    search_fields = ('name', 'category')

@admin.register(FlowLog)
class FlowLogAdmin(admin.ModelAdmin):
    list_display = ('product', 'action', 'quantity', 'timestamp')
    list_filter = ('action', 'timestamp')
    search_fields = ('product__name',)
    ordering = ('-timestamp',)
