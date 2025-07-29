'''4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.'''

import requests as re
from datetime import datetime


def converter_moedas(): 
    try: 
        cod = input('Digite o código da moeda: ')
        data = re.get(f'https://economia.awesomeapi.com.br/last/{cod}-BRL').json()
        
        key =  f'{cod}BRL'

        if key not in data: 
            raise ValueError(f"Moeda {cod} não encontrada.")
        
        info = data[key]
        
        information = { 
            'cotacao_atual': info['bid'],
            'valor_maximo': info['high'],
            'valor_minimo': info['low'], 
            'ultima_atualizacao': datetime.strptime(info['create_date'], "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")
        }

        return information
    
    except Exception as e: 
        print(f'Erro {e}') 


informacao = converter_moedas()
print(informacao)

