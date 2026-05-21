import pytest

from django.urls import reverse

@pytest.mark.django_db

def test_post_view(client):
    '''
    Função básica onde pega a url da home (base) e verificar se status da rede é 200 (OK)
    '''
    url = reverse('home')
    response = client.get(url)

    assert response.status_code == 200 