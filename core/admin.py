from django.contrib import admin
from core.models import  Post, Comment, Picture, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_date')
    list_filter = ()
    search_fields = ['title', 'content' ]
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    
    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ['title', ]


admin.site.register(Post, PostAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Category)

