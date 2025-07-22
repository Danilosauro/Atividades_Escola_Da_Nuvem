
reais = input('digite o valor em reais: ') 
taxa_dolar = 5.20 
taxa_euro = 6.15 

reais = float(reais)

valor_dolar = reais * taxa_dolar  
valor_euro = reais * taxa_euro 

print(f"Valor em dólar =  {valor_dolar:.2f}, valor em euro = {valor_euro:.2f}")