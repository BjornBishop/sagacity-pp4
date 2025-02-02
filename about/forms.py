from django import forms
from .models import CollaborationRequest

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborationRequest
        exclude = ('read',)
