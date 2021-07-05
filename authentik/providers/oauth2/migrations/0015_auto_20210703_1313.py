# Generated by Django 3.2.4 on 2021-07-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_providers_oauth2", "0014_alter_oauth2provider_rsa_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="authorizationcode",
            name="revoked",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="refreshtoken",
            name="revoked",
            field=models.BooleanField(default=False),
        ),
    ]