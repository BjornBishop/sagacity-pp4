from django.contrib import admin
from .models import ConsultingAssignment, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(ConsultingAssignment)
class ConsultingAssignmentAdmin(SummernoteModelAdmin): 
    list_display = ('title', 'slug', 'status', 'created_on', 'industry')
    list_filter = ('status', 'industry')
    search_fields = ('title', 'required_experience', 'role_description')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('required_experience', 'role_description') 

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('author', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'body')
    actions = ['approve_comments']
    summernote_fields = ('body',) 

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)