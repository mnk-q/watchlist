from django.shortcuts import get_object_or_404, render
from .models import People, Movie, MovieGenre
from django.views.generic import ListView
from .forms import SearchForm, MovieFilterForm
from datetime import datetime
from django.core.paginator import Paginator
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

def movie_filter(request):
    mvs={}
    if request.method=='GET':
        form2 = MovieFilterForm(request.GET)
        if form2.is_valid():
            g = request.GET['genre']
            if g=='all':
                g=''
            
            o ='-'+request.GET['orders']
            
            mvs = Movie.objects.filter(moviegenre__in=MovieGenre.objects.filter(mg_genre__contains=g), movie_release__lte=datetime.now()).distinct().order_by(o)
    else:
        form2 = MovieFilterForm()
    
    return render(request, 'movie/movie_filter.html', {'form2': form2, 'mvs': mvs})

class MovieUpcomingView(ListView):
    model = Movie
    template_name = 'movie/movie_upcoming.html'
    ordering = ["movie_release"]
    queryset = Movie.objects.filter(movie_release__gte=datetime.now())
    paginate_by = 4
    context_object_name = 'mvs'
    
def fourzerofour(request):

    return render(request, 'movie/404.html')


def test_area(request):
    mvs=[1,2,3]
    if request.method == 'POST':
        form = MovieFilterForm(request.POST)
        q1 = request.POST['genre']
        print(q1)
        
    else:
        form = MovieFilterForm()

    return render(request, 'movie/test_area.html', {'mvs': mvs, 'form': form})


class MovieListView(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    ordering = ["-movie_release"]
    queryset = Movie.objects.filter(movie_release__lte=datetime.now())
    paginate_by = 4
    context_object_name = 'mvs'
    
    

class HomepageList(ListView):
    model = Movie
    ordering = ['-movie_release']
    template_name = 'movie/home.html'
    