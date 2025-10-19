from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Use actual Post model field names (created_on, updated_on, content, status)
    list_display = ['title', 'author', 'created_on', 'updated_on', 'status']
    list_filter = ['created_on', 'status', 'author']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_on'
    ordering = ['-created_on']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Use actual Comment model field names (created_on, body, approved)
    list_display = ['post', 'author', 'created_on', 'approved']
    list_filter = ['approved', 'created_on']
    search_fields = ['author', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = 'Approve selected comments'

