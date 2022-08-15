# Generated by Django 4.0.6 on 2022-08-15 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0017_alter_ingredient_measurement_unit"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ingredient",
            options={
                "verbose_name": "Ингредиент",
                "verbose_name_plural": "Ингредиенты",
            },
        ),
        migrations.AlterModelOptions(
            name="ingredientamount",
            options={
                "verbose_name": "Количество ингридиента",
                "verbose_name_plural": "Количество ингридиентов",
            },
        ),
        migrations.AlterModelOptions(
            name="recipe",
            options={
                "ordering": ["-id"],
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
            },
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Тег", "verbose_name_plural": "Теги"},
        ),
    ]