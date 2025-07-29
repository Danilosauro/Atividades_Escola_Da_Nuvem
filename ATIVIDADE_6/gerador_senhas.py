'''1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.''' 


import random
import string

def gerar_senhas_aleatorias(): 
    try: 
        tamanho = int(input('Digite o tamanho desejado para a senha aleatória (quantidade de dígitos): '))
        digitos = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choices(digitos, k=tamanho))
        return senha
    except Exception as e: 
        print(f'Erro {e}') 


minha_senha_aleatoria = gerar_senhas_aleatorias()
print(minha_senha_aleatoria)
