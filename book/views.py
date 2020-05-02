from django.shortcuts import render
from book.models import RecipeItem, Author


# Create your views here.
def index(request):
    recipe_data = RecipeItem.objects.all()
    author_data = Author.objects.all()
    return render(request, 'index.html', {
        'recipe_data': recipe_data, "author_data": author_data})

def author(request, id):
    author_data = Author.objects.filter(id=id).first()
    recipe_data = RecipeItem.objects.filter(author=author_data)
    return render(request, 'author.html', {
        'author_data': author_data, 'recipe': recipe_data})

def recipes(request, id):
    recipe = RecipeItem.objects.filter(id=id).first()
    return render(request, "recipes.html", {"recipe": recipe})


