from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    idade = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


