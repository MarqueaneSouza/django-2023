from django.test import Client

def test_status_code(client:Client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_home_link(client: Client): #NÃO CONSEGUI DESENVOLVER O CÓDIGO PARA TESTE
    resp = client.get('/')
    assert resp.status_code == 200  # Verificar se a resposta foi bem-sucedida (código 200)
    assert b'<a href="/">Python Pro</a>' in resp.content  # Verificar se o link está no conteúdo da resposta
