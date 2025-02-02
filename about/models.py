from django.db import models
from django_summernote.fields import SummernoteTextField

class About(models.Model):
    title = models.CharField(max_length=200)
    content = SummernoteTextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
