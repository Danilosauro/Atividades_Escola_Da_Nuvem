'''4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.'''

from datetime import datetime


def calcula_idade_dias():
    try:
        ano_nascimento = int(input('Insira o ano de nascimento: '))
        ano_atual = datetime.now().year
        idade = ano_atual-ano_nascimento
        idade_em_dias = idade * 365

        return f'Idade : {idade}, Idade em dias: {idade_em_dias}'
    
    except Exception as e: 
        print(f'Erro {e}')

resultado = calcula_idade_dias()
print(resultado)