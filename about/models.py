from django.db import models
from django_summernote.fields import SummernoteTextField
from codestar.settings import custom_bleach_clean

class CustomSummernoteTextField(SummernoteTextField):
    def clean(self, value, *args, **kwargs):
        value = custom_bleach_clean(value)
        return super().clean(value, *args, **kwargs)

class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = CustomSummernoteTextField()

    def __str__(self):
        return self.title
