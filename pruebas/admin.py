from django.contrib import admin
from pruebas.models import Author, Book
# Register your models here.


class LibroAdmin(admin.ModelAdmin):
    # Esto crea una interfaz mucho más cómoda para elegir autores
    filter_horizontal = ('author',)


admin.site.register(Author)
admin.site.register(Book, LibroAdmin)
