from django.db import models

# Create your models here.

class Note(models.Model):
    titulo = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=200, blank=False, null=False)