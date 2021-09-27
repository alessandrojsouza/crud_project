from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Tarefa


# Create your views here.

# Lista todas as terefas e encaminha para página lista.html
def lista(request):
    tarefas = Tarefa.objects.all()
    return render (request, 'lista.html',{'tarefas':tarefas})


# Busca por um tarefa específica e encaminha para página tarefa.html
def tarefaView(request, id):
    tarefa = get_object_or_404 (Tarefa, pk=id)
    return render(request, 'tarefa.html',{'tarefa':tarefa})
