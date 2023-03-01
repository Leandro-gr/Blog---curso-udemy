from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'posted')
    list_filter = ('name','created', 'posted')
    date_hierarchy = 'posted'
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'posted', 'stats')
    list_filter = ('stats', 'created', 'posted', 'author')
    date_hierarchy = 'posted'
    raw_id_fields = ('author',)
    search_fields = ('title', 'posted')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
