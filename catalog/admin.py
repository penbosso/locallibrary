from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author
    

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
    
 
class BookInstanceResource(resources.ModelResource):
    class Meta:
        model = BookInstance

# admin.site.register(BookInstance)

class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

# Define the admin class
class AuthorAdmin(ImportExportModelAdmin):
    resource_class = AuthorResource
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(ImportExportModelAdmin):
    resource_class = BookInstanceResource
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )