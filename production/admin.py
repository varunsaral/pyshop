from django.contrib import admin
from .models import Prod,Offer


class ProdAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','disc')


admin.site.register(Prod, ProdAdmin)
admin.site.register(Offer, OfferAdmin)