# Generated by Django 4.2.18 on 2025-05-02 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posthog.models.utils


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0723_add_help_text_to_cohorts"),
    ]

    operations = [
        migrations.CreateModel(
            name="ErrorTrackingGroupingRule",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("bytecode", models.JSONField()),
                ("filters", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("disabled_data", models.JSONField(blank=True, null=True)),
                ("order_key", models.IntegerField()),
                ("description", models.TextField(null=True)),
                ("role", models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="ee.role")),
                ("team", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.team")),
                (
                    "user",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user_group",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="posthog.usergroup"),
                ),
            ],
            options={
                "indexes": [models.Index(fields=["team_id"], name="posthog_err_team_id_bf614f_idx")],
            },
        ),
    ]
