from django.shortcuts import render
from .models import Category, Author, Article
from django.views import generic



def index(request):
    num_articles = Articles.objects.all().count()
    num_authors = Authors.objects.all().count()


    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    

    return render(
        request,
        'index.html',
        context={'num_articles':num_articles,'num_authors':num_authors, 'num_visits':num_visits})