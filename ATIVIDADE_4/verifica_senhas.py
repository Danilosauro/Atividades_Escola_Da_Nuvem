'''3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".'''

def verifica_senha():
    try:
        senha = input('Insira uma senha com pelo menos 8 caracteres: ')
        
        if len(senha) < 8:
            print('Senha menor que oito caracteres.')
            return

        tem_digito = any(char.isdigit() for char in senha)
        letras = [char for char in senha if char.isalpha()]

        if not tem_digito:
            print('A senha deve conter ao menos um dígito.')
            return

        if len(letras) < 4:
            print('A senha deve conter ao menos quatro letras.')
            return

        print('Senha forte!')

    except Exception as e:
        print(f'Erro: {e}')

verifica_senha()
