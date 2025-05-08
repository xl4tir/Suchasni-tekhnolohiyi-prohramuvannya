from django.contrib import admin
from .models import Category, Article, ArticleImage

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'featured')
    search_fields = ('title', 'description')
    list_filter = ('category', 'featured')
    inlines = [ArticleImageInline]
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ArticleImage)
