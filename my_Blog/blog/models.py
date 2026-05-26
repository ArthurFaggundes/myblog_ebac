from django.db import models # necessária para criar tabelas e campos do banco de dados
from django.contrib.auth.models import User # importa o modelo de usuário padrão do Django (username, email, ...)

STATUS = ( # uma tupla, para ser substituida depois. ex: campo = 0 -> campo = Draft
    (0, 'Draft'),
    (1, 'Publish')
)

# Post.objects.all() = SELECT * FROM post;

class Post(models.Model): # CREATE TABLE post
    title = models.CharField(max_length=200, unique=True) # campo para texto pequeno || mesmo que: title VARCHAR(200)
    slug = models.SlugField(max_length=200, unique=True) # um pré-caminho da url ex: /meu-blog/"aprendendo-django-do-zero"/
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post') # on_delete=models.CASCADE -> Se o usuário for deletado todos os post feitos por ele são deletados
    updated_on = models.DateTimeField(auto_now=True) # Atualiza automaticamente toda vez que salvar
    content = models.TextField() # geralmente usado para campos grande, sem limitação de caracteres
    created_on = models.DateTimeField(auto_now_add =True) # Define data apenas na criação.
    status = models.IntegerField(choices=STATUS, default=0) # tipo um id (substitui automaticamente), inicia como Draft

    class Meta:
        ordering = ['-created_on'] # Ordena automaticamente os resultados em ordem decrescente

    def __str__(self):
        return self.title