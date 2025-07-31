""" Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
""" 

import json
import os

def ler_json():
    try: 
        nome = input('Insira o seu nome: ')
        idade = int(input('Insira a sua idade: '))
        cidade = input('Insira a sua cidade: ')

        dicionario = { 
            'nome': nome, 
            'idade': idade, 
            'cidade': cidade
        }
        
        file_name = str(input('Insira nome do arquivo para salvamento: ')).lower() 

        full_path = f"data/{file_name}"
        
        print(full_path)

        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(dicionario, f, ensure_ascii=False, indent=4)

        if file_name:
            with open(full_path, "r", encoding="utf-8") as f: 
                data = json.load(f)
                    
            return data
        else: 
            print("nenhum arquivo encontrado. O nome do arquivo está correto?")

    except Exception as e: 
        print(f'erro: {e}')


meus_dados = ler_json()
print(meus_dados)