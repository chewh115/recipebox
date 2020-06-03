from django.urls import path
from book import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipe_add/', views.recipe_add),
    path('author_add/', views.author_add),
    path('author/<int:id>/', views.author),
    path('recipes/<int:id>/', views.recipes),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('recipe_edit/<int:id>/', views.recipe_edit, name="recipe_edit"),
    path('favorite_recipe/<int:id>/', views.favorite_recipe, name="favorite"),
    path(
        'unfavorite_recipe/<int:id>/',
        views.unfavorite_recipe,
        name="unfavorite")
]
