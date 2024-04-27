from random import randint
robo = randint(1, 10)
resul = ''
vitoria = 0
while True:
    escolha = int(input('ESCOLHA UM NUMERO: '))
    parimp = str(input('PAR OU IMPAR [P/I]: ')).upper().strip()
    soma = escolha + robo
    teste = soma % 2
    
    
    if teste == 0:
        resul = 'Par'
    else:
        resul = 'Impar'
        
            
    if parimp == 'P' and resul == 'Par':
        print('Você ganhou eu escolhi {} e você {} somando {}'.format(robo, escolha, soma))
        vitoria += 1
    elif parimp == 'I' and resul == 'Impar':
        print('Você ganhou eu escolhi {} e você {} somando {}'.format(robo, escolha, soma))
        vitoria += 1
    else:
        print('Eu ganhei! eu escolhi {} e você {} somando {}'.format(robo, escolha, soma))
        break

print('Você ganhou {} vezes'.format(vitoria))