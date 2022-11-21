from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Note(models.Model):
    description = models.TextField(null=False)
    title = models.CharField(max_length=45, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    draft = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    saved = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:note_details`", args=(self.id))
