from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, CollaborationRequest
from .forms import CollaborateForm

def about_me(request):
    """
    Renders the About page with a form to submit collaboration requests
    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        form = CollaborateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application request has been submitted successfully. We should respond within the week')
            return redirect('about')
    else:
        form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "form": form},
    )
