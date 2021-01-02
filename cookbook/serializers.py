from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Recipe, Ingredient, Food


class FoodSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Food
        fields = ["id", "name"]


class IngredientSerializer(WritableNestedModelSerializer):
    quantity = serializers.CharField()
    food = FoodSerializer()

    class Meta:
        model = Ingredient
        fields = ["id", "quantity", "food"]


class RecipeSerializer(WritableNestedModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ["id", "name", "ingredients"]
