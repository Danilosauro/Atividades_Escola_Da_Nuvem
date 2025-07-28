'''3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.''' 

def calcula_desconto():
    try: 
        preco = float(input('Insira o preço do produto em reais: '))
        desconto = float(input('Insira o percentual de desconto desejado: '))
        valor_final  = preco - (desconto * preco) / 100 
        return f'Valor da compra com desconto: {valor_final:.2f} Reais'

    except Exception as e:
        print(f'erro: {e}')
    
desconto = calcula_desconto()
print(desconto)
