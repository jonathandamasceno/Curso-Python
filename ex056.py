soma_idade = 0
velho = 0
nome_v = ''
mulher20 = 0
for c in range(0, 4):
    c += 1
    print('-----{}ª PESSOA-----'.format(c))
    pessoa = str(input('NOME:')).strip().title()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]:')).strip().upper()
    soma_idade += idade
    media = soma_idade / c
    if c == 1:
        velho = idade
    else:
        if idade > velho and sexo == 'M':
            nome_v = pessoa
            velho = idade
    if idade < 20 and sexo == 'F':
        mulher20 += 1
                 
print('A media de idade das {} pessoas foi de {}.'.format(c, media))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nome_v))
print('Ao todo foram {} mulheres com menos de 20 anos.'.format(mulher20))