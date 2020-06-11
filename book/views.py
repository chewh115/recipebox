from django.shortcuts import render, reverse, HttpResponseRedirect
from book.models import RecipeItem, Author
from book.forms import RecipeAddForm, AuthorAddForm, LoginForm, RecipeEditForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
# don't use login name conventions over writing an import


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage'))
            )
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logoutview(request):
    if logout(request):
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'logout.html')


# Create your views here.
def index(request):
    recipe_data = RecipeItem.objects.all()
    author_data = Author.objects.all()
    return render(request, 'index.html', {
        'recipe_data': recipe_data, "author_data": author_data})


@login_required
def recipe_add(request):
    html = "recipe_add.html"

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
        # form.save()
        if form.is_valid():
            data = form.cleaned_data
            author = User.objects.create_user(
                username =data['name']
            )
            Author.objects.create(
                user=author,
                name=data['name'],
                bio=data.get('bio')
            )
        return HttpResponseRedirect(reverse("homepage"))
#works but if user already exist return to page. error showing
    return render(request, html, {"form": form})


def author(request, id):
    author_data = Author.objects.filter(id=id).first()
    data = RecipeItem.objects.all()
    return render(request, 'author.html', {
        'author_data': author_data, 'data': data})


def recipes(request, id):
    context = {}
    context['recipe'] = RecipeItem.objects.filter(id=id).first()
    if request.user.is_authenticated:
        context['user_data'] = Author.objects.get(name=request.user.username)
    return render(request, "recipes.html", context)


def recipe_edit(request, id):
    recipe = RecipeItem.objects.get(id=id)
    html = "recipe_edit.html"
    if request.user == recipe.author or request.user.is_staff:
        if request.method == "POST":
            form = RecipeEditForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                recipe.title = data['title']
                recipe.description = data['body']
                recipe.save()
                return HttpResponseRedirect(reverse('recipes', args=(id,)))
        form = RecipeEditForm(initial={
            'title': recipe.title,
            'body': recipe.description
        })
        return render(request, html, {'form': form, 'recipe': recipe})
    return render(request, html)


@login_required
def favorite_recipe(request, id):
    html = "recipes.html"
    if request.user.is_authenticated:
        user = Author.objects.get(name=request.user.username)
        recipe = RecipeItem.objects.get(id=id)
        user.favorites.add(recipe)
        user.save()
        return HttpResponseRedirect(reverse('recipes', args=(id,)))
    return render(request, html, {'user': user})


@login_required
def unfavorite_recipe(request, id):
    html = "recipes.html"
    if request.user.is_authenticated:
        user = Author.objects.get(name=request.user.username)
        recipe = RecipeItem.objects.get(id=id)
        user.favorites.remove(recipe)
        user.save()
        return HttpResponseRedirect(reverse('recipes', args=(id,)))
    return render(request, html)
