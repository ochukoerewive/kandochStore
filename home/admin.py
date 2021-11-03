from django.contrib import admin
from .models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'Image',
        'price',
        'Mileage',
        'Location',
        'Color',
        'Body Style',
        'transmition',
        'Engine',
        'Fuel',
    )

    ordering = ()

admin.site.register(Vendor)

