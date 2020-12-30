from django.contrib import admin
from core.models import  Post, Picture, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_date')
    list_filter = ()
    search_fields = ['title', 'content' ]
    prepopulated_fields = {'slug': ('title',)}


class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ['title', ]


admin.site.register(Post, PostAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Category)

