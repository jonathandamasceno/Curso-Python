km = int(input('DIGITE A DISTANCIA DA VIAGEM: '))
if km <= 200:
    taxa = km * 0.50
    
    print('O valor da viagem para {}km foi de R${:.2f}'.format(km, taxa))
else: 
    taxa = km * 0.45
    print('O valor da viagem para {}km foi de R${:.2f}'.format(km, taxa))