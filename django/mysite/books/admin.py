
from django.contrib import admin
from mysite.books.models import Publisher, Author, Book

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'website')
	list_filter = ('name',)
	search_fields = ('name',)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	list_filter = ('first_name', 'last_name',)
	search_fields = ('first_name', 'last_name',)

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher')
	list_filter = ('title', 'publisher',)
	search_fields = ('title',)
	filter_horizontal = ('authors',)

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

