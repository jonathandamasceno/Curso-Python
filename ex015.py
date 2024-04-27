dias = int(input('DIAS EM POSSE DO CARRO: '))
km = float(input('KM RODADOS: '))
preco = (dias * 60) + ( km * 0.15)
print('POR RODAR {}km EM {} DIAS, TERÁ QUE PAGAR R${}'.format(km, dias, preco)) 