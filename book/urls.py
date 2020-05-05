from django.urls import path
from book import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipeadd', views.recipeadd),
    path('author_add', views.author_add),
    path('author/<int:id>/', views.author),
    path('recipes/<int:id>/', views.recipes),
]
