
nome_do_produto = 'Cadeira Infantil'
preco_unitario = input('Digite o preço unitário:')
quantidade = input('Digite o a quantidade de produtos:')

preco_total = float(preco_unitario) * int(quantidade)

print(f'O valor total referente ao produto {nome_do_produto} é :R$ {preco_total:.2f}')