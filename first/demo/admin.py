from django.contrib import admin

from .models import Book, BookNumber, Character, Author

# Register your models here.

# admin.site.register(Book)

admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)


@admin.register(Book)
class BookDemo(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['published']
    