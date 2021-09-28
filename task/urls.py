
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaView ),
    path('tarefa/<int:id>', views.tarefaView),
    path('formCadastroTarefa/', views.formTarefaView),
    path('addTarefaView/', views.addTarefaView),
    path('delTarefa/<int:id>', views.delTarefaView),
    path('editTarefa/<int:id>', views.editTarefaView),
]
