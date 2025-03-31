from django.db import models
from django.contrib.auth.models import User

class Navigator(models.Model):
    nome = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Mentorados(models.Model):
    estagio_choices = (
        ('E1', '10 até 100k'),
        ('E2', '100k até 1M'),
        ('E3', '1M até 10M'),
        ('E4', '10M até 100M'),
        ('E5', '100M até 1B'),
        ('E6', '1B ou mais')
    )
    name = models.CharField(max_length=255)
    estagio = models.CharField(max_length=2, choices=estagio_choices)
    navigator = models.ForeignKey(Navigator, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
