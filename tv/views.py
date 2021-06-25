from django.shortcuts import render, HttpResponse

# Create your views here.
def testarea(request):
    return HttpResponse("<h1>Hello </h1>")

def tv_all(request):
    return HttpResponse("<h1>Hello </h1>")