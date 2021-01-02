from django.urls import path
from cookbook import views

app_name = "cookbook"
urlpatterns = [
    path("cookbook/recipes/", views.RecipeListView.as_view(), name="recipes"),
    path("cookbook/create_recipe/", views.RecipeCreateView.as_view(),
         name="create_recipe"),
    path("cookbook/destroy/<int:pk>/", views.DestroyView.as_view(),
         name="destroy"),
    path("cookbook/recipe/<int:pk>/", views.RetrieveRecipeView.as_view(),
         name="retrieve"),
]
