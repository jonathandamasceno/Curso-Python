barato = 0
n_barato = ''
total = 0   
c = caro = 0
while True:
    c += 1
    produto = str(input('DIGA O NOME DO PRODUTO: ')).title().strip()
    valor = float(input('VALOR DO PRODUTO: R$'))
    total += valor
    if c == 1:
        barato = valor
        n_barato = produto
    if valor < barato:
        barato = valor
        n_barato = produto
    if valor > 1000:
        caro += 1
    continuar = str(input('CONTINUAR? [S/N]: ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('CONTINUAR? [S/N]: '))
    if continuar == 'N':
        break
print('O total foi de R${:.2f}'.format(total))
print('O produto mais barato foi {} custando R${:.2f}'.format(n_barato, barato))
print('teve {} produto(s) custando mais de R$1000,00'.format(caro))