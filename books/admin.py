from django.contrib import admin

from .models import Volume

class VolumeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "publisher"]


admin.site.register(Volume, VolumeAdmin)