from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, \
    RetrieveAPIView

from cookbook.models import Recipe
from cookbook.serializers import RecipeSerializer


class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeCreateView(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class DestroyView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RetrieveRecipeView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
