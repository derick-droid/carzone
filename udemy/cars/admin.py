from django.contrib import admin
from .models import Cars
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
     # to bring photos
    def thumbnails(self, object):
        return format_html('<img src = "{}" width = " 40"/>'.format(object.car_photo.url))
    
    thumbnails.short_description = 'car image' # focusing on the heading of the photo
    list_display = ("id","thumbnails","car_title","city","colour", "Condition","model", "year", "body_style", "fuel_type", "is_featured")
    # making them linkable
    list_display_links = ("id", "thumbnails", "car_title")
    # making models of feature to be editable from the admin panel
    list_editable = ("is_featured",)
    # adding search category
    search_fields = ("id","car_title", "city", "models", "fuel_type")
    #adding filter
    list_filter = ("id", "city", "model", "fuel_type")
    
admin.site.register(Cars,CarAdmin)