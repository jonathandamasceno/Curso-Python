from random import randint
robo = randint(0,2)
print(robo)
jogada = ('Pedra', 'Papel', 'Tesoura') #lista pra saber o uqe que jogou
# não posso colocar a escolha sendo 1, 2 e 3 porque a lista começa sempre no 0
escolha = int(input('''ESCOLHA
[0] PEDRA
[1] PAPEL
[2] TESOURA
O QUE VOCÊ ESCOLHE: '''))
if escolha == robo:
    print('EMPATE')
    print('Você jogou {} e o robo jogou {}'.format(jogada[escolha], jogada[robo]))
if escolha == 1 and robo == 2 or escolha == 2 and robo == 3 or escolha == 3 and robo == 1:
    print('perdeu')
    print('Você jogou {} e o robo jogou {}'.format(jogada[escolha], jogada[robo]))
if robo == 1 and escolha == 2 or robo == 2 and escolha == 3 or robo == 3 and escolha == 1:
    print('Você ganhou')
    print('Você jogou {} e o robo jogou {}'.format(jogada[escolha], jogada[robo]))
print('Fim')