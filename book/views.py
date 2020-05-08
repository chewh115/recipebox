from django.shortcuts import render, reverse, HttpResponseRedirect
from book.models import RecipeItem, Author
from book.forms import RecipeAddForm, AuthorAddForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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


@login_required
def author_add(request):
    html = "author_add.html"
    form = AuthorAddForm()
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {"form": form})
else:
    return HttpResponse(status=201)


def author(request, id):
    author_data = Author.objects.filter(id=id).first()
    # recipe_data = RecipeItem.objects.filter(author=author_data)
    data = RecipeItem.objects.all()
    return render(request, 'author.html', {
        'author_data': author_data, 'data': data})


def recipes(request, id):
    recipe = RecipeItem.objects.filter(id=id).first()
    return render(request, "recipes.html", {"recipe": recipe})