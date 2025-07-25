'''4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.'''

def calcula_par_impar():
    try:
        numeros = []
        while True:
            nota = input('Insira uma número (ou "fim" para encerrar): ')
            if nota.lower() == 'fim':
                break
            numeros.append(float(nota)) 

            par = 0 
            impar = 0
            for numero in numeros: 
                resultado = numero % 2
                if resultado == 0:
                    print(f'O número {numero} é par.')
                    par +=1
                else: 
                    print(f'O número {numero} é ímpar.')
                    impar +=1
            print(f'Temos {par} números pares e {impar} números ímpares.')

    except Exception as e: 
        print(f'Erro {e}')

calcula_par_impar()