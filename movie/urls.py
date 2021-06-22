from django.urls import path, include
from .views import *
urlpatterns = [
    path('people/<str:slug>', people_view, name='people_detail'),
    path('movie/<str:slug>', movie_detail_view, name='movie_detail'),
    path('movies/all', MovieListView.as_view(), name='movies-all'),
    path('movies/search', movie_search, name='movie_search')
]
