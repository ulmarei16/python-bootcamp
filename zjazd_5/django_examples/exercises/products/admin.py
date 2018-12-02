from django.contrib import admin

# Register your models here.
from django.contrib import admin
#tutaj dodaje rzeczy do panelu adminstratora

from products.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["operation", "param1", "param2"]
    search_fields = ["operation"]
    list_filter = ["operation"]

admin.site.register(Math, MathAdmin)