cont = 0
lista = [0,0,0,0,0]
soma = 0
while True:
    num = int(input('DIGITE UM NUMERO: '))
    if 0 <= num <= 1000:
        lista[cont] = num
        cont += 1
        if cont == 1:
            soma += num
    if cont == 5:
        break
if soma > lista[0]:
    print('Dados inválidos. Por favor reinicie.')
else:
    print(lista[0] - sum(lista[1:]))