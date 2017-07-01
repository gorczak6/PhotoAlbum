from django.contrib import admin

from album.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

