from django.shortcuts import render, get_object_or_404
from todoapi.models import ToDo, User

def kanban_list(request):
    todos = ToDo.objects.all()
    return render(request, 'kanban_list.html', {'todos': todos})

def kanban_detail(request, kanban_name):
    todo = get_object_or_404(ToDo, kanban_name=kanban_name)
    columns = todo.columns.all().order_by('position')  # Ordenar por posição
    return render(request, 'kanban_detail.html', {'todo': todo, 'columns': columns})

