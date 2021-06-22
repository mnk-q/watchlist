from django.shortcuts import get_object_or_404, render
from .models import People, Movie
from django.views.generic import ListView
from .forms import SearchForm
# Create your views here.

def people_view(request, slug):
    q = get_object_or_404(People.objects.filter(people_slug=slug))
    context = {
        'q': q
    }
    return render(request, 'movie/people.html', context)

def movie_detail_view(request, slug):
    q = get_object_or_404(Movie, movie_slug=slug)
    context = {
        "movie": q
    }

    return render(request, 'movie/movie_detail.html', context)

def movie_search(request):
    obj={}
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            obj = Movie.objects.filter(movie_title__contains=request.GET['search'].title())
            print(obj)
    else:
        form = SearchForm()
    
    return render(request, 'movie/movie_search.html', {'form': form, 'obj': obj} )

class MovieListView(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    ordering = ["-movie_release"]
    queryset = Movie.objects.all()
    context_object_name = 'mvs'
    paginate_by = 4

class HomepageList(ListView):
    model = Movie
    ordering = ['-movie_release']
    template_name = 'movie/home.html'
    