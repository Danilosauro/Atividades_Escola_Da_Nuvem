'''1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.'''


def calculadora():
    try:
        numero_um = input('Insira um número: ') 
        operacao = input('Insira a operação desejada: ')
        numero_dois = input('Insira o segundo número: ')
        numero_um = int(numero_um)
        numero_dois = int(numero_dois) 

        if operacao == '+': 
            resultado = numero_um + numero_dois
            print(resultado)
        if operacao == '-': 
            resultado = numero_um - numero_dois
            print(resultado)
        if operacao == '*': 
            resultado = numero_um * numero_dois
            print(resultado)
        if operacao == '/': 
            resultado = numero_um/numero_dois
            print(resultado)

    except ValueError: 
        print('Insira apenas números. Retorne')
        calculadora()
    except ZeroDivisionError: 
        print('Impossível dividir por zero. Retorne')
        calculadora()

calculadora()
