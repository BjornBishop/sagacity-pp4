from django.urls import path
from blog.views import ConsultingAssignmentList, ConsultingAssignmentDetail

urlpatterns = [
    path('', ConsultingAssignmentList.as_view(), name='home'),
    path('assignment/<slug:slug>/', ConsultingAssignmentDetail.as_view(), name='assignment_detail'),
]