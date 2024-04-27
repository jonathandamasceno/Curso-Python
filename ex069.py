mulheres = homens = maior = 0
while True:
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).upper().strip()
    continuar = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()
    
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if continuar == 'N':    
        break
print('total de pessoas com mais de 18 anos = {}'.format(maior))
print('{} homens cadastrados'.format(homens))
print('total de {} mulheres com menos de 20 anos'.format(mulheres))
