# Generated by Django 4.0.6 on 2022-07-31 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0009_alter_ingredient_measurement_unit_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="IngredientAmount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.ImageField(upload_to="", verbose_name="Количество"),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.ingredient",
                        verbose_name="Ингредиент",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Название"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="media/recipes/images/",
                        verbose_name="Картинка",
                    ),
                ),
                ("text", models.TextField(verbose_name="Описание")),
                (
                    "cooking_time",
                    models.IntegerField(verbose_name="Время приготовления (в минутах)"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор рецепта",
                    ),
                ),
                (
                    "ingredients",
                    models.ManyToManyField(
                        to="recipes.ingredientamount",
                        verbose_name="Список ингредиентов",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        to="recipes.tag", verbose_name="Список тегов"
                    ),
                ),
            ],
        ),
    ]