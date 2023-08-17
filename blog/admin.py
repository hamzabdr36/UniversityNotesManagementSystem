from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file', 'author', 'date_posted']
    list_filter = ('author', 'date_posted')


admin.site.register(Post, PostAdmin)


