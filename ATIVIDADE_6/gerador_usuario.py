'''2- Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.'''

import requests as re

def gerar_usuario_aleatorio():
    try:
        usuarios = re.get("https://randomuser.me/api/").json()
        usuario = usuarios['results'][0]
        usuario_final = {
            "nome" : f"{usuario['name']['first']} {usuario['name']['last']}",
            "email" : usuario['email'],
            "pais" : usuario['location']['country']} 

        return usuario_final
    except Exception as e:
        print(f'Erro {e}')

meu_usuario_aleatorio = gerar_usuario_aleatorio()
print(meu_usuario_aleatorio)