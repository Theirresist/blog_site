from django.contrib import admin
from .models import Category, Author, Article



admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Category)

'''
@admin.site.register(Category)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    fieldsets = (
        ('Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth')}))



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_category')
    list_filter = ('category',)
    	
'''