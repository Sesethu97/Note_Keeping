# Generated by Django 4.1.3 on 2022-11-05 14:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Note",
            new_name="Notes",
        ),
    ]
