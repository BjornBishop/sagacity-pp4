from django.urls import path
from blog.views import ConsultingAssignmentList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assignments/', ConsultingAssignmentList.as_view(), name='assignment_list'), 
]