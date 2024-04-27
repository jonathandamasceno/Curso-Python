# PA - v3.0
pt = int(input('DIGITE O PRIMEIRO TERMO: '))
r = int(input('DIGITE A RAZÃO: '))
n_termos = int(input('DIGITE O NUMERO DE TERMOS: '))
mais = 0
c = 0
while c < n_termos:
    c += 1
    print('{}° termo - {}'.format(c, pt))
    pt += r
    if c == n_termos:
        mais = int(input('QUER MAIS QUANTOS TERMOS?[0 PARA]: '))
        n_termos += mais
print('Fim')
print('foram {} termos mostrados.'.format(c))