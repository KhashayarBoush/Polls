from django.contrib import admin
from . import models

class BookInline(admin.TabularInline):
    model = models.Book
    extra  = 1

@admin.register(models.Writer)
class WriterAdmin(admin.ModelAdmin):
    #fields  = [('name','family')]
    fieldsets = (
        ('personal infomartion', {
            'fields': ('name', 'family')
        }),
        ('Availability', {
            'fields': ('Email', 'born')
        })
    )
    list_display = ['name', 'family', 'Email']
    list_filter = [ 'name', 'Email']

    inlines  = [BookInline]



@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'writer', 'id']
    list_filter = [ 'name', 'writer']
