from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('RecipeItem', symmetrical=False, blank=True, related_name='favorite_recipe')

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=15)
    instructions = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title