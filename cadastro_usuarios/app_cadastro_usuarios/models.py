import uuid
from django.db import models

class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    area_atuacao = models.CharField(max_length=100)
