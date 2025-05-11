from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','status','publish']
    list_filter = ['status', 'created', 'publish', 'auteur']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['auteur']
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    show_facets = admin.ShowFacets.ALWAYS
    search_fields = ['title']
