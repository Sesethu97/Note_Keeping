from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Note(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='saved')

    status_code = (
        ('draft', 'Draft'),('saved', 'Saved'),

    ) 
    title = models.CharField(max_length=45, null=False)
    description = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status_code = models.CharField(max_length=15, choices=status_code, default='draft')
    important = models.ManyToManyField(User, related_name="important", default=None, blank=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manage

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:note_details`", args=(self.id))
