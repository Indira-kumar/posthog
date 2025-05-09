# Generated by Django 4.2.18 on 2025-02-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0662_alter_batchexport_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="insightvariable",
            name="type",
            field=models.CharField(
                choices=[
                    ("String", "String"),
                    ("Number", "Number"),
                    ("Boolean", "Boolean"),
                    ("List", "List"),
                    ("Date", "Date"),
                ],
                max_length=128,
            ),
        ),
    ]
