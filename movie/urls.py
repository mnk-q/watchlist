from django.urls import path, include
from .views import *
urlpatterns = [
    path('', HomepageList.as_view(), name='home'),
    path('people/<str:slug>', people_view, name='people_detail'),
    path('movie/<str:slug>', movie_detail_view, name='movie_detail'),
    path('movies/all', MovieListView.as_view(), name='movies-all'),
    path('movies/filter', movie_filter, name='movie_filter'),
    path('movies/search', movie_search, name='movie_search'),
    path('movies/upcoming', MovieUpcomingView.as_view(), name='movie_upcoming'),
    path('404', fourzerofour, name='404'),
    path('test', test_area, name='test_area')
]
