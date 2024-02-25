from django.contrib import admin

from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'menu_name')
    list_filter = ('menu_name',)

    verbose_name = 'Пункт меню'
    verbose_name_plural = 'Пункты меню'


admin.site.register(MenuItem, MenuItemAdmin)
