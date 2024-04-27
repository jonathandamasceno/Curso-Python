c = 0
soma = 0
qtd_n = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
        qtd_n += 1
print('Fim!')
print('A SOMA DOS {} NUMEROS FOI DE {}'.format(qtd_n, soma))