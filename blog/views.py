from django.shortcuts import render
from django.views import generic
from .models import ConsultingAssignment

# Create your views here.
class ConsultingAssignmentList(generic.ListView):
    queryset = ConsultingAssignment.objects.all()
    template_name = 'assignments/post_list.html'  
    context_object_name = 'assignments'  