'''
contador 
1 - > De 1 a 10, de 1 em 1
2 - > De 10 a 0, de 2 em 2
3 - > contagem personalizada
'''
from time import sleep
def contagem(ini, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    #sleep(1)
    cont = ini
    if ini <= fim:
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True) # pro sleep() funcionar 
            cont += passo
        print()  
    else:
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True) # pro sleep() funcionar 
            cont -= passo
        print()  
        
        
contagem(1, 10, 1)
contagem(10, 1, -1)
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(ini, fim, passo)