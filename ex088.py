'''
Sorteando numeros da mega sena
'''

from random import randint
from time import sleep
jogo_unico = []
jogos = []
numero_jogos = int(input('DIGITE A QUANTIDADE DE JOGOS QUE DESEJA SORTEAR: '))
for c in range (1, numero_jogos):
    cont = 0
    while True:
        num = (randint( 1, 60))
        if num not in jogo_unico:
            jogo_unico.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo_unico.sort()
    jogos.append(jogo_unico[:])
    jogo_unico.clear()
cont = 0
for t in jogos:
    cont += 1
    print(f'Jogo {cont}: {t}')
    sleep(1.5)