from django.urls import path, include
from .views import *

urlpatterns = [
    path('', testarea, name='testarea'),
    path('all', tv_all, name='tv_all')
    

]
