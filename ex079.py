'''
digitar varios valores e colocar numa lista
se o numero ja estiver lá, ele não é adicionado
no fim mostrar a lista completa em ordem crescente (numeros)
'''
c = 0
lista = list()
resp = 'S'
while resp == 'S':
    lista.append(int(input('DIGITE UM NÚMERO: ')))
    if lista.count(lista[c]) > 1:
        print('Número já foi adicionado, não será contabilizado.')
        lista.pop(c)
    else:
        print('Número adicionado com sucesso')
        c += 1  
    resp = str(input('QUER CONTINUAR? [S/N]')).strip().upper()
    while resp not in 'SN':
        resp = str(input('DIGITE UMA OPÇÃO VáLIDA: [S/N]')).strip().upper()
    if resp in 'N':
        break
lista.sort()
print(lista)
# dava pra fazer:
'''
numeros = (int(input('DIGITE UM NÚMERO: ')))
if numeros not in lista:
    lista.append(numeros)
    print('NUMERO ADICIONADO.')
else:
    print('Numero duplicado.')
'''