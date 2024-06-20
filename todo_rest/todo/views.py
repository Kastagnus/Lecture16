from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Todo

def todo_list(request):

    todos = Todo.objects.all()
    data = {'todos': list(todos.values())}

    return JsonResponse(data)

def todo_detail(request, pk):

    try:
        todo = Todo.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse(
            {'Status code': 404, 'Message': f'todo list with id {pk} does not exist'}
        )
    else:
        data = {'todo':todo.id,
                'title': todo.title,
                'completed': todo.completed,
                'user': todo.user.username
                }

        return JsonResponse(data)




# Create your views here.
