num = c = soma = 0
while True:
    num = int(input('DIGITE UM NUMERO: '))
    if num == 999:
        break  
    soma += num
    c += 1
print('A quantidade de termos foi de {} e a soma foi de {}'.format(c, soma))