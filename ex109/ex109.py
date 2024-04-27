import moeda

preco = float(input('Digite o preço: '))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'Aumentando 10% de {moeda.moeda(preco)}.... Ficou: {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 13% de {moeda.moeda(preco)}.... Ficou: {moeda.diminuir(preco, 13, True)}')