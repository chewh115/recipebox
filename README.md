# recipebox


# For our introduction, we want to get familiar with creating a new Django application. Create a new application that serves recipes from different authors, much like our demo application does for news. Intended layout:

An index page that lists all titles of the loaded recipes (they don't have to be real recipes; just fill them with lorem ipsum and some numbers.)
Each title is a link that takes you to a single page with the content of that recipe.
Each detail view for a recipe has the author name, along with all the information for the recipe arranged in a reasonable format.
Clicking on the author's name should take you to an Author Detail page, where you can see a list of all the recipes that Author has contributed to.
Make editing all of the models accessible through the admin panel only.
So we have three types of pages: a simple list view, a recipe detail view, and an author detail view. The admin panel will handle the creation views, so we don't need to worry about that.

Important Info:

Python 3.8, latest version of Django (3.0.5 as of this writing)
Start a project with `django-admin startproject {project name} .` -- note the period at the end! (for example, `django-admin startproject recipebox .`)
Start the server with `python manage.py runserver`
After you create your models, run `python manage.py makemigrations {foldername}` (where foldername is the top level folder for your project) to create them, then `python manage.py migrate` to push them to the db. If you get stuck, delete the db and run the command again
If you change your models after running the migrations, run makemigrations and migrate again. If the migrations require the creation of a new table, django will automatically handle it
Create an admin user by running `python manage.py createsuperuser`
Don't go crazy on the front end. The goal is to just handle the database interactions and basic view path
Make sure that every detail page (author and recipe) has its own unique URL. If you reload the URL, the same page should appear -- no modals or manipulating the current information on the page. That's too complicated for what we're trying to achieve.
REITERATING: There are no extra points for pretty HTML! Don't spend time making everything on the front end look gorgeous; we just want to make sure we're serving the right information.
Please don't commit any extraneous files! It's best practice to use a .gitignore file to keep a clean repository. See the this link (Links to an external site.)Links to an external site. for what you should include in your .gitignore file.
Author model:

Name (CharField)
Bio (TextField)
Recipe Model:

Title (CharField)
Author (ForeignKey)
Description (TextField)
Time Required (Charfield) (for example, "One hour")
Instructions (TextField)

<p>
<br>-- Run off environment </br>
<br>run the command line</br>
<br>-- python manage.py runserver</br>

<br>localhost:800</br>
<br>localhost:8000/admin</br>
</p>