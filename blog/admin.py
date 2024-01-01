from django.contrib import admin
from . import models

@admin.register(models.BlogModel)
class AdminBlog(admin.ModelAdmin):
    list_display = ["user", "title", "slug", "show_image"]
    list_filter = ["user", "slug"]
    search_fields = ["title", "description"]
    list_per_page = 5

@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["blog", "date"]
    search_fields = ["blog"]
    list_per_page = 10