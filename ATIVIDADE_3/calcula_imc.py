'''Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
''' 


peso = input('Insira o seu peso em kilos: ')
altura = input('Insira a sua altura em metros: ') 

peso = float(peso)
altura = float(altura)

imc = peso/(altura*altura)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >18.5 and imc <25:
    print('Peso normal')
elif imc >25 and imc <30: 
    print('Sobrepeso')
else: 
    print('Obeso')