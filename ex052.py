num = int(input('DIGITE UM NUMERO: '))
cont = 0
for c in range (1, num+1):
    if num % c == 0:
        print(num / c, end=' -> ')
        cont += 1
if cont == 2:
    print('É UM NUMERO PRIMO')
else: 
    print('NAO É UM NUMERO PRIMO') 
print('O numero {} foi dividido {} vezes.'.format(num, cont))