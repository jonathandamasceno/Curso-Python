nota = 50
qtd_notas = 0
saque = float(input('QUANTOS REAIS VAI SACAR? R$'))
total = saque
while True:
    if total >= nota:
        total -= nota
        qtd_notas += 1
    else:
        print('precisa de {} notas de {}'.format(qtd_notas, nota))
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        qtd_notas = 0    
        if total == 0: 
            break