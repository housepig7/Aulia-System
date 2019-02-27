from django.contrib import admin
from .models import *
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Prop', {'fields': ['propname', 'propnumber', 'propprice']}),
        ('id', {'fields': ['playerid', 'orderid']})
    ]
    list_display = ('playerid', 'orderid', 'rechargetime', 'givingtime', 'confirmtime')
    list_filter = ['rechargetime']
    search_fields = ['rechargetime']


class ArchivesAdmin(admin.ModelAdmin):
    list_display = ('user', 'channel', 'time')


class CircularAdmin(admin.ModelAdmin):
    list_display = ('game', 'title', 'time')


class OrderPpAdmin(admin.ModelAdmin):
    fieldsets = [
        ('id', {'fields': ['billno', 'order_id']}),
        ('player', {'fields': ['account', 'rechargetime', 'givingtime']})
    ]
    list_display = ('account', 'order_id', 'billno', 'rechargetime', 'givingtime')
    list_filter = ['rechargetime']
    search_fields = ['order_id']


admin.site.register(Order, OrderAdmin)
admin.site.register(Circular, CircularAdmin)
admin.site.register(Archives, ArchivesAdmin)
admin.site.register(OrderPp, OrderPpAdmin)
admin.site.site_header = 'Aulia\'s System'
admin.site.site_title = 'Aulia\'s System'
admin.site.index_title= 'Welcome to Aulia\'s System'