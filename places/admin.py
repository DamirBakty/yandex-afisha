from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ('get_preview',)
    fields = ('id', 'image', 'get_preview',)

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
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
    readonly_fields = ('image',)

    def image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
        ))

admin.site.register(PlaceImage)
