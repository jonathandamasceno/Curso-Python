from random import randint
robo = (randint(1,50), randint(1,50), 
        randint(1,50), randint(1,50), 
        randint(1,50), randint(1,50))
tupla = robo
org = sorted(tupla)
maior = org[-1] # ou max(tupla)
menor = org[0]  # ou min(tupla)
print(f'O maior valor foi {maior} e o menor foi {menor}')
print(tupla, end=' ')