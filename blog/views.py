from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import ConsultingAssignment

class ConsultingAssignmentList(generic.ListView):
    queryset = ConsultingAssignment.objects.filter(status__in=[1, 2])  # Filter out Draft (0) and Closed (3)
    template_name = 'assignments/index.html'
    context_object_name = 'assignments'
    paginate_by = 6

class ConsultingAssignmentDetail(generic.DetailView):
    model = ConsultingAssignment
    template_name = 'assignments/detail.html'