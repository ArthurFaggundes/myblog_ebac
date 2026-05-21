from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    '''
    Modelo base de uma View (página da Web)
    '''
    def get(self, request, **kwargs):
        return None