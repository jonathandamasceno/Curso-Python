produto = float(input('diga o valor do produto: '))
desc = produto - (produto * 0.05)
print('O produto que custava {}, agora custa {:.2f}.'.format(produto, desc))