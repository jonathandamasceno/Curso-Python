from random import randint
from time import sleep
jogador = int(input('diga qual numero estou pensando: '))
robo = randint(1, 5)
sleep(2)
if jogador != robo:
    print('EU GANHEI!!')
    print('Eu pensei no número {}'.format(robo))
else:
    print('VOCÊ GANHOU!!')