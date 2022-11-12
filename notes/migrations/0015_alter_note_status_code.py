# Generated by Django 4.1.3 on 2022-11-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0014_alter_note_status_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="status_code",
            field=models.CharField(
                choices=[("saved", "Saved"), ("draft", "Draft")],
                default="draft",
                max_length=15,
            ),
        ),
    ]