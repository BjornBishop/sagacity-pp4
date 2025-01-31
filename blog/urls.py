from django.urls import path
from blog.views import ConsultingAssignmentList

urlpatterns = [
    path('assignments/', ConsultingAssignmentList.as_view(), name='assignment_list'),
]