# Generated by Django 4.0.6 on 2022-08-01 13:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0002_subscription_delete_follow"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="subscription",
            unique_together={("user", "author")},
        ),
    ]