from django.urls import path, include
from .views import *

urlpatterns = [
    path('test', testarea, name='testarea'),
    path('', TVListView.as_view(), name='tv_all'),
    path('<str:slug>', tv_detail, name='tv-detail')
    
]
