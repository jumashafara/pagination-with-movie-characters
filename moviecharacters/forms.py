# import django modal forms
from django.forms import ModelForm
from moviecharacters.models import Movie
from moviecharacters.models import Character

# create the form class
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre']


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['movie', 'name', 'age', 'first_appearance']

