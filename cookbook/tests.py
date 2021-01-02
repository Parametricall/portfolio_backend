from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .models import Recipe, Ingredient, Food

CREATE_RECIPE_URL = reverse("cookbook:create_recipe")
GET_RECIPES_URL = reverse("cookbook:recipes")


class PublicRecipeAppTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_recipe(self):
        payload = {
            "name": "Test",
            "ingredients": [{
                "food": {
                    "name": "Carrot"
                },
                "quantity": "12"
            }]
        }
        res = self.client.post(CREATE_RECIPE_URL, payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED, res.content)
        recipe = Recipe.objects.get(pk=res.json()["id"])
        self.assertEqual(recipe.name, payload["name"])

        ingredients = Ingredient.objects.filter(recipe=recipe)
        self.assertEqual(len(ingredients), 1)

        food = Food.objects.filter(name='Carrot')
        self.assertEqual(len(food), 1)

    def test_get_recipes(self):
        recipe = Recipe.objects.create(name="New Recipe")
        food = Food.objects.create(name="Carrot")
        Ingredient.objects.create(
            food=food,
            quantity=1,
            recipe=recipe
        )

        res = self.client.get(GET_RECIPES_URL, format='json')

        json = res.json()[0]

        self.assertEqual(json, {
            "id": 1,
            "name": "New Recipe",
            "ingredients": [
                {
                    "id": 1,
                    "quantity": '1',
                    "food": {
                        "id": 1,
                        "name": "Carrot"
                    }
                }
            ]
        })
