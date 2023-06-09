from django.db import models

# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    link = models.URLField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo