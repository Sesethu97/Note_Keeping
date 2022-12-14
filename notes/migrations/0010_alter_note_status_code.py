# Generated by Django 4.1.3 on 2022-11-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0009_alter_note_status_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="status_code",
            field=models.CharField(
                choices=[("draft", "Draft"), ("saved", "Saved")],
                default="draft",
                max_length=15,
            ),
        ),
    ]
