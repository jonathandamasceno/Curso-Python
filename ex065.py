esc = 'S'
c = 0
num = soma = 0
maior = menor = 0
while esc == 'S':
    num = int(input('DIGITE UM NUMERO: '))
    esc = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()
    while esc != 'S' and esc != 'N':
        esc = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()
    soma += num
    c += 1
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
media = soma / c
print('A media foi de {}.'.format(media))
print('A quantidade de termos foi {}'.format(c))
print('O maior termo foi {} e o menor foi {}'.format(maior, menor))