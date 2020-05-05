from django.urls import path
from book import views


urlpatterns = [
    path('', views.index),
    path('recipe_add/', views.recipeadd),
    path('author/<int:id>/', views.author),
    path('recipes/<int:id>/', views.recipes),
]
