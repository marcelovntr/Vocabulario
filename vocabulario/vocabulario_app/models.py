from django.db import models

# Create your models here.
class Word(models.Model):

    FREQUENCIA_TIPOS = [
        ('alta', 'alta'),
        ('media', 'media'),
        ('baixa', 'baixa'),
    ]

    vocabulo = models.CharField(max_length=100)
    significado = models.CharField(max_length=200)
    exemplo = models.CharField(max_length=200)
    frequencia = models.CharField(max_length=20, choices=FREQUENCIA_TIPOS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"English Words({self.vocabulo}, {self.frequencia}, {self.significado})"
    # ou assim: self.vocabulo + ' - ' + self.significado
