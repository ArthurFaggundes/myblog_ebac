from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'crated_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields =  {'slug': ('title',)} # para preencher o slug com o mesmo conteudo do title

admin.site.register(Post)