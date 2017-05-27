from __future__ import unicode_literals

from django.contrib import admin

from models import Day


class DayAdmin(admin.ModelAdmin):
    list_display = ['owner', 'date']

admin.site.register(Day, DayAdmin)
