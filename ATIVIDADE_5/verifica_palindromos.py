'''2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.'''


def verifica_palindromos():
    try:
        resultado = ''
        palavra = input('Insira a palavra ou frase a ser avalida: ')
        palavra = palavra.lower()
        reversed_iterator = reversed(palavra)
        palavra_revertida = "".join(reversed_iterator)

        for letra in palavra: 
            for artel in palavra_revertida:
                if letra == artel:
                    resultado = 'sim'
                else: 
                    resultado = 'não'

        return resultado 

    except Exception as e:
        print(f'erro {e}')

teste = verifica_palindromos()
print(teste)
