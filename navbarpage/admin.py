from django.contrib import admin
from . import models

@admin.register(models.ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    list_filter = ("email",)
    list_per_page = 10
    search_fields = ("name", "email", "phone")

admin.site.register(models.AboutModel)
admin.site.register(models.OurStory)
admin.site.register(models.OurPartners)
admin.site.register(models.OurTeam)