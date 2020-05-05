from django import forms
from book.models import Author


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']