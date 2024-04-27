from random import randint
print('PENSEI EM UM NUMERO.')
num = int (input('TENTE ADIVINHAR: '))
robo = randint(1, 5)
cont = 0
while num != robo:
    cont += 1
    if num > robo:
        num = int (input('MENOS... TENTE ADIVINHAR: '))
    if num < robo:
        num = int (input('MAIS... TENTE ADIVINHAR: '))
        
print('foram {} tentativas, você acertou, eu escolhi {}.'.format(cont, robo))
    
    