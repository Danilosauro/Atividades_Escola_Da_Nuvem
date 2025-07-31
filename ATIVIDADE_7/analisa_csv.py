import pandas as pd 
import glob

""" 
Crie um programa que analisa um arquivo CSV contendo dados de execução de um processo de treinamento. O programa deve:

* Solicitar ao usuário o nome do arquivo CSV (ex: logs_treinamento.csv).  
* Ler os dados usando a biblioteca `pandas`.  
* Calcular a média e o desvio padrão da coluna `tempo_execucao`.  
* Exibir os resultados com duas casas decimais.  
* Tratar erros como arquivo inexistente ou formatação incorreta.

Dica: Use `df['coluna'].mean()` e `df['coluna'].std()` para obter os resultados estatísticos."""

# criando o arquivo

logs_treinamento = pd.DataFrame(
    {
    "tempo_execucao":[5,10,20,30]
    }
    )

logs_treinamento.to_csv('data/logs_treinamento.csv', header=True, encoding='UTF-8')

# leitura do arquivo para análise 

def analisa_arquivo():
    try: 
        nome = input('Insira o nome do arquivo: ')
        nome = str(nome).lower()
        base_path = 'data' + '/' + nome
        print(base_path)

        if base_path:
            logs = pd.read_csv(base_path)
                    
            information = { 
                'média': logs['tempo_execucao'].mean().round(2), 
                'desvio_padrao': logs['tempo_execucao'].std().round(2)
                }
                
            return information
        else: 
            print("nenhum arquivo encontrado. O nome do arquivo está correto?")

    except Exception as e: 
        print(f'erro: {e}')


analise = analisa_arquivo() 
print(analise)