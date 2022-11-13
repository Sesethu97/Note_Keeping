# Generated by Django 4.1.3 on 2022-11-13 17:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notes", "0019_remove_note_status_code_note_draft_note_saved"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="important",
            field=models.ManyToManyField(
                blank=True, related_name="important", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
