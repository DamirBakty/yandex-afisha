from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    readonly_fields = ('get_preview',)
    fields = ('order', 'image', 'get_preview')

    def get_preview(self, obj):
        max_height = 200
        height = obj.image.height
        if height > max_height:
            height = 200

        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height=height,
        ))


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['title']
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'image')
