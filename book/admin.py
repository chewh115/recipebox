from django.contrib import admin

from book.models import Author, RecipeItem
# Register your models here.
admin.site.register(Author)
admin.site.register(RecipeItem)