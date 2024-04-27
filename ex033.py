valor1 = int(input('DIGITE UM VALOR: '))
valor2 = int(input('DIGITE UM VALOR: '))
valor3 = int(input('DIGITE UM VALOR: '))
maior = valor1
menor = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor2 and valor3 > valor1:
    maior = valor3
#////
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor2 and valor3 < valor1:
    menor = valor3
print('O maior numero é {} e o menor é {}'.format(maior, menor))