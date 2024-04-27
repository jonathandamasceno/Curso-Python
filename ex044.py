valor = float(input('QUAL O VALOR DO PRODUTO? '))
escolha = int(input('''COMO IRÁ PAGAR?
[1] À VISTA DINHEIRO / CHEQUE 
[2] À VISTA CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO
SUA ESCOLHA: '''))

if escolha == 1:
    desconto = valor - (valor * 0.1)
    print('VOCÊ ESCOLHEU À VISTA DINHEIRO/CHEQUE')
    print('A COMPRA NO VALOR DE R${:.2f} COM 10% DE DESCONTO VAI CUSTAR R${:.2f}'.format(valor, desconto))
elif escolha == 2:
    desconto = valor - (valor * 0.05)
    print('VOCÊ ESCOLHEU À VISTA CARTÃO')
    print('A COMPRA NO VALOR DE R${:.2f} COM 5% DE DESCONTO VAI CUSTAR R${:.2f}'.format(valor, desconto))
elif escolha == 3:
    parcela = valor / 2
    print('VOCÊ ESCOLHEU 2X NO CARTÃO')
    print('A COMPRA NO VALOR DE R${:.2f} EM 2X FICOU COM PARCELAS DE R${:.2f}'.format(valor, parcela))
elif escolha == 4:
    vezes = int(input('EM QUANTAS PARCELAS? '))
    aumento = valor + (valor * 0.2)
    parcela = aumento / vezes
    print('A COMPRA NO VALOR DE R${:.2f} COM 20% DE JUROS EM {} VEZES DE R${} VAI CUSTAR R${:.2f}'.format(valor, vezes, parcela, aumento))

