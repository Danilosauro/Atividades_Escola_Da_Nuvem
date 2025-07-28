''''1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.''' 


def calcula_gorgeta():
    try:
        conta = float(input('Insira o valor da conta em reais: '))
        gorgeta = conta * (10/100)
        return f'A sua gorgeta 10% é : {gorgeta:.2f} Reais'
    
    except Exception as e:
        print(f'erro: {e}')

gorgeta = calcula_gorgeta()
print(gorgeta)
