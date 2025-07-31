"""2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha."""


import csv

dados_pessoas = [
    ["João Silva", 28, "São Paulo"],
    ["Maria Oliveira", 34, "Rio de Janeiro"],
    ["Carlos Souza", 22, "Belo Horizonte"]
]

headers = ["Nome", "Idade", "Cidade"]

nome_arquivo = input("Digite o nome do arquivo CSV que deseja salvar: ")

try:
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file_csv:
        escritor = csv.writer(file_csv)
        escritor.writerow(headers)  
        escritor.writerows(dados_pessoas)

    print(f"Dados gravados com sucesso em '{nome_arquivo}'.")

except Exception as e:
    print(f"Erro ao gravar o arquivo: {e}")
