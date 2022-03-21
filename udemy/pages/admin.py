
from django.contrib import admin
from django.utils.html import format_html # customizing photo
from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    # to bring photos
    def thumbnails(self, object):
        return format_html('<img src = "{}" width = " 40"/>'.format(object.photos.url))
    
    thumbnails.short_description = 'photo' # focusing on the heading of the photo
    
    list_display = ('id', 'thumbnails', 'first_name', 'last_name', 'designation','created_date')
    list_display_links = ('id', 'thumbnails','first_name', 'last_name', 'designation', 'created_date')
    # adding search field
    search_fields = ('first_name', 'last_name', 'designation')
    # adding filter box
    list_filter = ('designation',)
admin.site.register(Team,TeamAdmin)

