from .models import Movie
from .forms import MovieForm
from .models import Character
from .forms import CharacterForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator

# Create your views here.
def movies(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('moviecharacters:movies')
    else:
        movies = Movie.objects.all()
        paginator = Paginator(movies, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'movies': page_obj, 'form':form}
        template_name = 'movies.html'
    return render(request, template_name=template_name, context=context)
    
def characters(request, movie_id):
    form = CharacterForm(initial={'movie': movie_id})
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['movie'] = movie
            form.save()
        else:
            print('ERROR OCCURED!!!')
        return redirect(to='moviecharacters:characters', movie_id=movie_id)
    else:
        characters = Character.objects.filter(movie=movie)
        paginator = Paginator(characters, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'characters': page_obj, 'form':form, 'movie': movie}
        template_name = 'characters.html'
    return render(request=request, template_name=template_name, context=context)
