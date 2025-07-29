'''3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: .  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.'''

import requests as re

def consulta_cep(): 
    try: 
        cep = int(input('Digite o cep para busca (Apenas números): '))
        
        resultado = re.get(f"https://viacep.com.br/ws/{cep}/json/").json()

        if 'erro' in resultado:
            raise ValueError("CEP não encontrado.")
        
        endereco_completo = { 
            'logradouro': resultado['logradouro'], 
            'bairro': resultado['bairro'],
            'cidade': resultado['localidade'], 
            'estado': resultado['uf'], 
            'cep': resultado['cep']
        }
    
        return endereco_completo

    except ValueError as ve:
        print(f"Erro de validação: {ve}")
    except re.exceptions.Timeout:
        print("Erro: Tempo de resposta excedido.")
    except re.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return None

endereco = consulta_cep()
print(endereco)

