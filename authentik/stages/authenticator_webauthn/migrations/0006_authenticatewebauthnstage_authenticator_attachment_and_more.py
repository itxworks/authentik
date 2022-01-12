# Generated by Django 4.0.1 on 2022-01-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "authentik_stages_authenticator_webauthn",
            "0005_authenticatewebauthnstage_user_verification",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="authenticatewebauthnstage",
            name="authenticator_attachment",
            field=models.TextField(
                choices=[("platform", "Platform"), ("cross-platform", "Cross Platform")],
                default=None,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="authenticatewebauthnstage",
            name="resident_key_requirement",
            field=models.TextField(
                choices=[
                    ("discouraged", "Discouraged"),
                    ("preferred", "Preferred"),
                    ("required", "Required"),
                ],
                default="preferred",
            ),
        ),
    ]