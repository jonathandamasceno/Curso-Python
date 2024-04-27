lado1 = float(input('DIGITE O VALOR DO 1° SEGMENTO: '))
lado2 = float(input('DIGITE O VALOR DO 2° SEGMENTO: '))
lado3 = float(input('DIGITE O VALOR DO 3° SEGMENTO: '))

if lado1 > lado2 + lado3 and lado2 > lado1 + lado3 and lado3 > lado2 + lado1:
    print('NÃO FORMA UM TRIANGULO')
else:
    print('FORMA UM TRIANGULO')
