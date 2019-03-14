from django.contrib import admin
from . import models

class Tabular(admin.TabularInline):
    model  = models.Choice
    extra = 1


@admin.register(models.Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ['text','date']
    inlines  = [Tabular]

@admin.register(models.Choice)
class AdminChoice(admin.ModelAdmin):
    list_display =  ['question','text','vots']
