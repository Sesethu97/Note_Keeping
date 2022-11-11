from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Note(models.Model):
    status_code = {
        ('draft', 'Draft'),('saved', 'Saved'),

    }
    title = models.CharField(max_length=45, null=False)
    description = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status_code = models.CharField(max_length=15, choices=status_code, default='draft')
    # importance = models.ManyToManyField(User, related_name="important", default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:post_details", args=(self.id))
