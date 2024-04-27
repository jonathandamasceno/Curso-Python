vel = int(input('VELOCIDADE DO CARRO: '))
if vel <= 80:
    print('Continue seguindo as leis de transito')
if vel > 80:
    multa = (vel - 80) * 7
    print('Você terá que pagar uma multa.')
    print('O valor é de R${:.2f}'.format(multa))