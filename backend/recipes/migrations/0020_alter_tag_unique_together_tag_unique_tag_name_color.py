# Generated by Django 4.0.6 on 2022-08-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "recipes",
            "0019_alter_favorite_options_alter_recipe_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="tag",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="tag",
            constraint=models.UniqueConstraint(
                fields=("name", "color"), name="unique_tag_name_color"
            ),
        ),
    ]