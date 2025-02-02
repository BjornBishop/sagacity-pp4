from django.contrib import admin
from .models import ConsultingAssignment, Comment, CollaborationRequest

class ConsultingAssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status')
    search_fields = ('title', 'required_experience', 'role_description')
    list_filter = ('status', 'created_on', 'industry')
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'content')

@admin.register(CollaborationRequest)
class CollaborationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_on', 'read')
    list_filter = ('read', 'submitted_on')
    search_fields = ('name', 'email')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected requests as read"

admin.site.register(ConsultingAssignment, ConsultingAssignmentAdmin)
admin.site.register(Comment, CommentAdmin)
