from django.shortcuts import render
from django.http import HttpResponse
#import databse model
from .models import TodoItem

# Create your views here.

def todoView(request):
    allItems = TodoItem.objects.all()
    return render(request, 'todo.html', {'allItems': allItems})
