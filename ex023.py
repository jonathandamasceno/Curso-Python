num = int(input('INFORME UM NUMERO: '))
print('analisando o numero {}'.format(num))

mil = num // 1000 % 10
cen = num // 100 % 10
dez = num // 10 % 10
un = num // 1 % 10

print('a unidade é {}'.format(un))
print('a dezena é {}'.format(dez))
print('a centena é {}'.format(cen))
print('a unidade milhar é {}'.format(mil))