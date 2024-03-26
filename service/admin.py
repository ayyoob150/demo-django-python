from django.contrib import admin
from service.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price' , 'description')
    
admin.site.register(Product,ProductAdmin)

# Register your models here.
