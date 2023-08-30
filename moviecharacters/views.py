from .models import Character
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def rickAndMorty(request):
    characters = Character.objects.filter(movie='Rick and Morty')
    paginator = Paginator(characters, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'characters': page_obj, 'movie':'Rick and Morty'}
    return render(request, 'characters.html', context=context)