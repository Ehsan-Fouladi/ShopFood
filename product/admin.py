from django.contrib import admin
from . import models

@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "image")
    list_filter = ("title",)
    list_per_page = 9
    search_fields = ("title",)