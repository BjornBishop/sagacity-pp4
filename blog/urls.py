from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConsultingAssignmentList.as_view(), name='home'),
    path('assignment/<slug:slug>/', views.ConsultingAssignmentDetail.as_view(), name='assignment_detail'),
    path('assignment/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('assignment/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
