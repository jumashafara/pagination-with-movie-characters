from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
app_name = 'moviecharacters'

urlpatterns = [
    path('', views.movies, name='movies'),
    path('<int:movie_id>/', views.characters, name='characters')
]
