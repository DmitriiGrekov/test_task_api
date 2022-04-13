from django.contrib import admin
from .models import CommentModel, PostModel


admin.site.register(PostModel)


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author_name')
