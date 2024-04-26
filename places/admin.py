from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    readonly_fields = ('get_preview',)
    fields = ('order', 'get_preview', 'image')

    def get_preview(self, obj):
        height = obj.image.height
        width = obj.image.width

        formatted_html = format_html(
            '<img style="max-height: 200px; max-width: 200px;" src="{}" height="{}" width="{}"/> />',
            obj.image.url,
            height,
            width
        )
        return formatted_html



@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['title']
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'image')
    autocomplete_fields = ("place",)

