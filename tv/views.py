from typing import List
from django.db.models import query
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import *
# Create your views here.
def testarea(request):
    return HttpResponse("<h1>Hello </h1>")

class TVListView(ListView):
    model = TVShow
    template_name = 'tv/tv_all.html'
    queryset = TVShow.objects.all()
    paginate_by = 5
    context_object_name = 'mvs'

def tv_detail(request, slug):
    tv = TVShow.objects.get(tv_slug = slug)
    context = {'tv': tv}

    return render(request, 'tv/tv_detail.html', context)

