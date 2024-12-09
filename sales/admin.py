from django.contrib import admin
from .models import Customer, Product, Producttype, Bill, Order

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter=['first_name', 'last_name']
    list_display=['first_name', 'last_name']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Producttype)
admin.site.register(Bill)
admin.site.register(Order)