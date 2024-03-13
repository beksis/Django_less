from django.contrib import admin
from .models import CategoryModel
from .models import NewsModel

# admin.site.register() Возможно прописать как этот???


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at']
    search_fields = ['category_title']
    list_filter = ['created_at']
    ordering = ['pk']


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['news_title', 'news_created_at']
    ordering = ['pk']
# Register your models here.
