from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from users.serializers import CustomUserSerializer

from .models import Ingredient, IngredientAmount, Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "color",
            "slug",
        ]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            "id",
            "name",
            "measurement_unit",
        ]


class IngredientAmountSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(),
    )
    name = serializers.CharField(source="ingredient.name")
    measurement_unit = serializers.CharField(
        source="ingredient.measurement_unit",
    )

    class Meta:
        model = IngredientAmount
        fields = [
            "id",
            "name",
            "measurement_unit",
            "amount",
        ]


class RecipeReadSerializer(serializers.ModelSerializer):
    tags = TagSerializer(
        many=True,
        read_only=True,
    )
    author = CustomUserSerializer(required=False)
    ingredients = IngredientAmountSerializer(
        many=True,
        required=False,
    )
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = [
            "id",
            "tags",
            "author",
            "ingredients",
            "is_favorited",
            "is_in_shopping_cart",
            "name",
            "image",
            "text",
            "cooking_time",
        ]

    def get_is_favorited(self, obj):
        return False

    def get_is_in_shopping_cart(self, obj):
        return False


class IngredientAmountWriteSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        source="ingredient", queryset=Ingredient.objects.all()
    )

    class Meta:
        model = IngredientAmount
        fields = [
            "id",
            "amount",
        ]


class RecipeWriteSerializer(serializers.ModelSerializer):
    ingredients = IngredientAmountWriteSerializer(
        many=True,
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
    )
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = [
            "ingredients",
            "tags",
            "image",
            "name",
            "text",
            "cooking_time",
        ]

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        ingredients_data = validated_data.pop("ingredients")
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags_data)

        ingredient_amounts = []
        for item in ingredients_data:
            ingredient = item.get("ingredient")
            amount = item.get("amount")
            ingredient_amount, _ = IngredientAmount.objects.get_or_create(
                ingredient=ingredient,
                amount=amount,
            )
            ingredient_amounts.append(ingredient_amount)
        recipe.ingredients.set(ingredient_amounts)
        return recipe

    def update(self, instance, validated_data):
        instance.ingredients.clear()
        instance.tags.clear()
        tags_data = validated_data.pop("tags")
        ingredients_data = validated_data.pop("ingredients")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.tags.set(tags_data)
        ingredient_amounts = []
        for item in ingredients_data:
            ingredient = item.get("ingredient")
            amount = item.get("amount")
            ingredient_amount, _ = IngredientAmount.objects.get_or_create(
                ingredient=ingredient,
                amount=amount,
            )
            ingredient_amounts.append(ingredient_amount)
        instance.ingredients.set(ingredient_amounts)
        return instance
