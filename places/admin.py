from django.contrib import admin

from places.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


@admin.register(Place)
class SubdivisionAdmin(admin.ModelAdmin):
    # list_display = ['coordinates']
    inlines = [PlaceImageInline]

admin.site.register(PlaceImage)
