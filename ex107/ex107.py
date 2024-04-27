import moeda

preco = float(input('Digite o preço: '))
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'Aumentando 10% de {preco}... fica: {moeda.aumentar(preco, 10)}')
print(f'Diminuindo 13% de {preco}... fica: {moeda.diminuir(preco, 13)}')
