from django.urls import path
from blog.views import ConsultingAssignmentList

urlpatterns = [
    path('', ConsultingAssignmentList.as_view(), name='home'),
]