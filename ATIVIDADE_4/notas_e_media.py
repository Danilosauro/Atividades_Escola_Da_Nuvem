'''2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.'''

def calcula_media():
    try:
        notas = []
        while True:
            nota = input('Insira uma nota (ou "fim" para encerrar): ')
            if nota.lower() == 'fim':
                break
            notas.append(float(nota))
        
        if notas:
            media = sum(notas) / len(notas)
            print(f'A média final do estudante é: {media:.2f}')
        else:
            print('Nenhuma nota foi inserida.')
    except ValueError:
        print('Insira valores válidos.')
        calcula_media()

calcula_media()


