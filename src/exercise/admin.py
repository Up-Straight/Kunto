from __future__ import unicode_literals

from django.contrib import admin

from models import Exercise, State


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']


class StateAdmin(admin.ModelAdmin):
    list_display = ['exercise']

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(State, StateAdmin)