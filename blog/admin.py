from django.contrib import admin
from .models import ConsultingAssignment

# Register your models here.

@admin.register(ConsultingAssignment)
class ConsultingAssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'industry')
    list_filter = ('status', 'industry')
    search_fields = ('title', 'required_experience', 'role_description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)