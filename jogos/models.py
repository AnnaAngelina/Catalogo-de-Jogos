from django.db import models


class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Desenvolvedora"
        verbose_name_plural = "Desenvolvedoras"

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    nome = models.CharField(max_length=60)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    ano_lancamento = models.PositiveIntegerField()
    desenvolvedora = models.ForeignKey(
        Desenvolvedora,
        on_delete=models.CASCADE,
        related_name="jogos"
    )
    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.CASCADE,
        related_name="jogos"
    )

    class Meta:
        ordering = ["nome"]
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"

    def __str__(self):
        return self.nome
