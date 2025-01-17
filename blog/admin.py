from django.contrib import admin

from blog.models import Comment, Tag, Post, AuthorProfile

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')

admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(AuthorProfile)


# Register your models here.
