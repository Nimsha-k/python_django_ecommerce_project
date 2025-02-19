from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Category
from .models import Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','slug','image','stock','available','created','updated',]
    list_editable = ['price','stock','available']
    prepopulated_fields={'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)

