from django.contrib import admin
from .models import Menu, Category


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    list_filter = ['category']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category)
