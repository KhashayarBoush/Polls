from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
