from django.contrib import admin
from .models import Genre, Author, Article





admin.site.register(Genre)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    fieldsets = (
    	('Information', {
    		'fields': ('first_name', 'last_name')
    		}),
    	('Life', {
    		'fields': ('date_of_birth', )
    		}),
    	)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('title',)
