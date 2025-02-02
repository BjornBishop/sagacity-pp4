from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import ConsultingAssignment
from .forms import CommentForm

class ConsultingAssignmentList(generic.ListView):
    queryset = ConsultingAssignment.objects.filter(status__in=[1, 2])  # Filter out Draft (0) and Closed (3)
    template_name = 'assignments/index.html'
    context_object_name = 'assignments'
    paginate_by = 6

class ConsultingAssignmentDetail(generic.DetailView):
    model = ConsultingAssignment
    template_name = 'assignments/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_count'] = comment_count
        context['comment_form'] = comment_form
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            
            # Add success message
            messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')
            
            return redirect('assignment_detail', slug=post.slug)

        context = self.get_context_data()
        context['comment_form'] = comment_form
        return self.render_to_response(context)
