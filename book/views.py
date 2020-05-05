from django.shortcuts import render, reverse, HttpResponseRedirect
from book.models import RecipeItem, Author
from book.forms import RecipeAddForm, AuthorAddForm


# Create your views here.
def index(request):
    recipe_data = RecipeItem.objects.all()
    author_data = Author.objects.all()
    return render(request, 'index.html', {
        'recipe_data': recipe_data, "author_data": author_data})


def recipeadd(request):
    html = "recipeadd.html"

    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                description=data['body'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeAddForm()

    return render(request, html, {"form": form})


def author_add(request):
    html = "author_add.html"
    form = AuthorAddForm()
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {"form": form})


def author(request, id):
    author_data = Author.objects.filter(id=id).first()
    # recipe_data = RecipeItem.objects.filter(author=author_data)
    data = RecipeItem.objects.all()
    return render(request, 'author.html', {
        'author_data': author_data, 'data': data})


def recipes(request, id):
    recipe = RecipeItem.objects.filter(id=id).first()
    return render(request, "recipes.html", {"recipe": recipe})

