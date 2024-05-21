from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home (request):
    movies=Movie.objects.all()
    context ={
        'movies':movies,
    }
    return render(request,'app/index.html',context)
