maior = menor = 0 

for c in range(0, 5):
    c += 1
    peso = float(input('PESO DA {}ª PESSOA: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso 
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso foi de {} e o maior foi de {}.'.format(menor, maior))