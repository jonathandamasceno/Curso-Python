from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'Jogador1': randint(1, 6),
         'Jogador2': randint(1, 6),
         'Jogador3': randint(1, 6),
         'Jogador4': randint(1, 6)
}
# organizar o dicionario
organizado = {}
print('Valores sorteados: ')
print('-'*30)
for k, v in jogo.items():
    print(f'     {k} : {v}')
    sleep(0.5)
organizado = sorted(jogo.items(),key=itemgetter(1), reverse=True )
print('-'*30)
print('Ranking...')
for posicao, valores in enumerate(organizado):
    print(f'{posicao + 1}º Lugar: {valores[0]} escolheu {valores[1]}')
    sleep(1)