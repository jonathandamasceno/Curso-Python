casa = float(input('VALOR DA CASA: '))
salario = float(input('SEU SALARIO MENSAL: '))
anos = int(input('EM QUANTOS ANOS VAI PAGAR: '))
prest = casa / (anos * 12)
limite = salario * 0.3
print('Pra pagar a casa no valor de R${:.2f} em {} anos a prestação seria de R${:.2f}.'.format(casa, anos, prest))
if prest > limite:
    print('NÃO POSSO EMPRESTAR')
else:
    print('EMPRESTIMO ACEITO')

