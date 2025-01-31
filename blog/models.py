from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Qualified"),
    (2, "Needs requalification"),
    (3, "Closed")
)

INDUSTRY_CHOICES = (
    ("FS", "Financial Services"),
    ("COM", "Commercial"),
    ("MAN", "Manufacturing")
)

class ConsultingAssignment(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="consulting_assignments"
    )
    required_experience = models.TextField()
    role_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    industry = models.CharField(max_length=3, choices=INDUSTRY_CHOICES)

    def save(self, *args, **kwargs):
        # Automatically set excerpt to required_experience
        self.excerpt = self.required_experience
        super().save(*args, **kwargs)

# Comment model
class Comment(models.Model):
    post = models.ForeignKey(ConsultingAssignment, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'