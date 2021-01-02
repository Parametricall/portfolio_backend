from django.db import models


class Recipe(models.Model):
    name = models.CharField(
        max_length=255
    )


class Food(models.Model):
    name = models.CharField(max_length=255)


class Ingredient(models.Model):
    # food = models.OneToOneField(Food, on_delete=models.PROTECT)
    quantity = models.CharField(max_length=255)
    food = models.ForeignKey(
        to=Food,
        related_name="food",
        on_delete=models.PROTECT,
    )
    recipe = models.ForeignKey(
        to=Recipe,
        related_name="ingredients",
        on_delete=models.CASCADE,
    )
