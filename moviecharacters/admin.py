from .models import Movie
from .models import Character
from django.contrib import admin

# Register your models here.
admin.site.register(model_or_iterable=[Movie, Character])