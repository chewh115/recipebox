from django.db import models
from django.utils import timezone


# Create your models here.
""" 
Author model:

Name (CharField)
Bio (TextField)
Recipe Model:

Title (CharField)
Author (ForeignKey)
Description (TextField)
Time Required (Charfield) (for example, "One hour")
Instructions (TextField)

"""

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

class RecipeItem(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=15)
    instructions = models.TextField()
    date = models.DateTimeField(default=timezone.now)