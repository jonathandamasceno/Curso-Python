c = soma = num = 0
num = int(input('digite um numero: '))
while num != 999:
    c += 1
    soma += num
    num = int(input('digite um numero: '))
print('FORAM DIGITADOS {} NUMEROS E A SOMA FOI DE {}.'.format(c, soma))