from django.shortcuts import render
from django.http import HttpResponseRedirect
#import databse model
from .models import TodoItem

# Create your views here.

def todoView(request):
    allItems = TodoItem.objects.all()
    return render(request, 'todo.html', {'allItems': allItems})
    #we have to add this view to url.py

def addTodo(request):
    #create new todoItem
    #save to databse
    #redirect back to todo.html

    #in the post request we recieved get the attribute that has name content
    c = request.POST['content']
    new_todo = TodoItem(content = c)
    new_todo.save()
    return HttpResponseRedirect('/todo/')
    #we have to now map this view to url.py

def deleteTodo(request, todoID):
    itemToDelete = TodoItem.objects.get(id = todoID)
    itemToDelete.delete()
    return HttpResponseRedirect('/todo/')
