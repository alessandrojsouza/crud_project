from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    data =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo