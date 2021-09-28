from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarefa
from django.utils import timezone

# Create your views here.

# Lista todas as terefas e encaminha para página lista.html
def listaView(request):
    tarefas = Tarefa.objects.all()
    return render (request, 'lista.html',{'tarefas':tarefas})


# Busca por um tarefa específica e encaminha para página tarefa.html
def tarefaView(request, id):
    tarefa = get_object_or_404 (Tarefa, pk=id)
    return render(request, 'tarefa.html',{'tarefa':tarefa})

def formTarefaView(request):
    return render(request, 'formCadastroTarefa.html')

# Adiciona tarefa
def addTarefaView(request):
    # recupera informações do formulário
    titulo = request.POST['titulo']
    descricao = request.POST['descricao']
    data = timezone.now()

    tarefa = Tarefa(titulo=titulo,descricao=descricao, data=data)
    tarefa.save()
    return redirect('/')

# Exclui uma tarefa
def delTarefaView(request, id):
    tarefa = get_object_or_404 (Tarefa, pk=id)
    tarefa.delete()
    return redirect('/')

# Edita uma tarefa   
def editTarefaView(request, id):
    # recupera informações do formulário
    tarefa = get_object_or_404 (Tarefa, pk=id)

    # veifica se a solicitação é POST
    if (request.method == 'POST'):
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        data = timezone.now()

        tarefa = Tarefa(titulo=titulo,descricao=descricao, data=data)
        tarefa.save()
        return redirect('/')

    return render(request, 'editTarefa.html',{'tarefa':tarefa})