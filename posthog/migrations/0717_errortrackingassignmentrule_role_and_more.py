# Generated by Django 4.2.18 on 2025-04-24 11:37

from django.db import migrations, models
import django.db.models.deletion

# # ORIGINAL migration
# class Migration(migrations.Migration):
#     dependencies = [
#         ("ee", "0026_conversation_created_at_conversation_title_and_more"),
#         ("posthog", "0716_backfill_team_revenue_analytics_config"),
#     ]

#     operations = [
#         migrations.AddField(
#             model_name="errortrackingassignmentrule",
#             name="role",
#             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="ee.role"),
#         ),
#         migrations.AddField(
#             model_name="errortrackingissueassignment",
#             name="role",
#             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="ee.role"),
#         ),
#     ]


class Migration(migrations.Migration):
    atomic = False  # Added to support concurrent index creation
    dependencies = [
        ("ee", "0026_conversation_created_at_conversation_title_and_more"),
        ("posthog", "0716_backfill_team_revenue_analytics_config"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AddField(
                    model_name="errortrackingassignmentrule",
                    name="role",
                    field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="ee.role"),
                ),
                migrations.AddField(
                    model_name="errortrackingissueassignment",
                    name="role",
                    field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="ee.role"),
                ),
            ],
            database_operations=[
                # We add -- existing-table-constraint-ignore to ignore the constraint validation in CI.
                migrations.RunSQL(
                    """
                    ALTER TABLE "posthog_errortrackingassignmentrule" ADD COLUMN "role_id" uuid NULL CONSTRAINT "posthog_errortrackin_role_id_5faac145_fk_ee_role_i" REFERENCES "ee_role"("id") DEFERRABLE INITIALLY DEFERRED; -- existing-table-constraint-ignore
                    SET CONSTRAINTS "posthog_errortrackin_role_id_5faac145_fk_ee_role_i" IMMEDIATE; -- existing-table-constraint-ignore
                    """,
                    reverse_sql="""
                        ALTER TABLE "posthog_errortrackingassignmentrule" DROP COLUMN IF EXISTS "role_id";
                    """,
                ),
                migrations.RunSQL(
                    """
                    ALTER TABLE "posthog_errortrackingissueassignment" ADD COLUMN "role_id" uuid NULL CONSTRAINT "posthog_errortrackin_role_id_f84c52d3_fk_ee_role_i" REFERENCES "ee_role"("id") DEFERRABLE INITIALLY DEFERRED; -- existing-table-constraint-ignore
                    SET CONSTRAINTS "posthog_errortrackin_role_id_f84c52d3_fk_ee_role_i" IMMEDIATE; -- existing-table-constraint-ignore
                    """,
                    reverse_sql="""
                        ALTER TABLE "posthog_errortrackingissueassignment" DROP COLUMN IF EXISTS "role_id";
                    """,
                ),
                # We add CONCURRENTLY to the create command
                migrations.RunSQL(
                    """
                    CREATE INDEX CONCURRENTLY "posthog_errortrackingassignmentrule_role_id_5faac145" ON "posthog_errortrackingassignmentrule" ("role_id");
                    """,
                    reverse_sql="""
                        DROP INDEX IF EXISTS "posthog_errortrackingassignmentrule_role_id_5faac145";
                    """,
                ),
                migrations.RunSQL(
                    """
                    CREATE INDEX CONCURRENTLY "posthog_errortrackingissueassignment_role_id_f84c52d3" ON "posthog_errortrackingissueassignment" ("role_id");
                    """,
                    reverse_sql="""
                        DROP INDEX IF EXISTS "posthog_errortrackingissueassignment_role_id_f84c52d3";
                    """,
                ),
            ],
        ),
    ]
