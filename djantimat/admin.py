from djantimat.models import Slang, TraceBrowser
from django.contrib import admin


@admin.register(Slang)
class SlangAdmin(admin.ModelAdmin):
    list_display = ['word']
    search_fields = ['word']


@admin.register(TraceBrowser)
class TraceBrowserAdmin(admin.ModelAdmin):
    list_display = ['uniqueid']
    search_fields = ['uniqueid']
