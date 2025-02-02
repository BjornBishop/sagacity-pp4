from django.urls import path
from blog.views import ConsultingAssignmentList, ConsultingAssignmentDetail, comment_edit

urlpatterns = [
    path('', ConsultingAssignmentList.as_view(), name='home'),
    path('assignment/<slug:slug>/', ConsultingAssignmentDetail.as_view(), name='assignment_detail'),
    path('assignment/<slug:slug>/edit_comment/<int:comment_id>/', comment_edit, name='comment_edit'),
]
