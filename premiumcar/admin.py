from django.contrib import admin

from .models import *

admin.site.register(Category)


class ProductImageStackedInline(admin.TabularInline):

    model = ImageCar
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'short_description',
        'category'
    )

    inlines = [ ProductImageStackedInline]

# Register your models here.
