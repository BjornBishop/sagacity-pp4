from django.contrib import admin
from .models import ConsultingAssignment, Comment

class ConsultingAssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status')
    search_fields = ('title', 'required_experience', 'role_description')
    list_filter = ('status', 'created_on', 'industry')
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'content')

# Register your models here
admin.site.register(ConsultingAssignment, ConsultingAssignmentAdmin)
admin.site.register(Comment, CommentAdmin)
