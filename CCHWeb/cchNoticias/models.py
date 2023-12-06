from django.db import models

# Create your models here.


class Noticias(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='images/',default="")
    imagem2 = models.ImageField(upload_to='images/',default="")
    # imagem1 = models.TextField(max_length=50, default="")
    # imagem2 = models.TextField(max_length=50, default="")

    descricao = models.TextField()
    corpo = models.TextField()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):

    mensagem = models.TextField(max_length=300)
    blog = models.ForeignKey(Noticias, default="", on_delete=models.CASCADE, related_name='cmm')

    def __str__(self):
        return self.mensagem
