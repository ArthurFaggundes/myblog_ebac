import pytest
import json

from django.urls import reverse

@pytest.mark.django_db

def test_post_view(client):
    '''
    Função básica onde pega a url da home (base) e verificar se status da rede é 200 (OK) e se tem o texto na tela
    '''
    url = reverse('home')
    response = client.get(url)

    assert response.status_code == 200

    response = json.loads(response.content)
    assert response.content == 'Hello World'