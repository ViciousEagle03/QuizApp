# Generated by Django 5.1.4 on 2024-12-17 16:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0008_quizsession_current_question"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quizsession",
            name="total_questions",
        ),
        migrations.AddField(
            model_name="quizsession",
            name="end_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="quizsession",
            name="start_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
