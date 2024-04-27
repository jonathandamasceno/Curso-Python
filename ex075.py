par = 0
num = (int(input('DIGITE UM 1º NÚMERO: ')),
        int(input('DIGITE UM 2º NÚMERO: ')),
        int(input('DIGITE UM 3º NÚMERO: ')),
        int(input('DIGITE UM 4º NÚMERO: ')))
print(f'Os numeros pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
        par += 1
print(f'\nA quantidade de numeros pares foi de {par}.')        
print(f'os numeros digitados foram {num}')
print(f'numeros digitados colocados em ordem {sorted(num)}')
print(f'O numero 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O numero 3 foi digitado na posição {num.index(3) + 1}.')
else:
    print(f'O numero 3 nao foi digitado.')

'''
jeito que eu tinha feito
par = 0
num1 = int(input('DIGITE UM 1º NÚMERO: '))
num2 = int(input('DIGITE UM 2º NÚMERO: '))
num3 = int(input('DIGITE UM 3º NÚMERO: '))
num4 = int(input('DIGITE UM 4º NÚMERO: '))
tupla = (num1 , num2 , num3 , num4)

if tupla[0] % 2 == 0:
    par += 1
if tupla[1] % 2 == 0:
    par += 1
if tupla[2] % 2 == 0:
    par += 1
if tupla[3] % 2 == 0:
    par += 1
'''