from . import views
from django.urls import path
from .views import ConsultingAssignmentList

urlpatterns = [
    path('assignments/', ConsultingAssignmentList.as_view(), name='assignment_list'),
]