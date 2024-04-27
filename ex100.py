from random import randint
from time import sleep

def sorteia(lista):
    for cont in range(0,5):
        lista.append(randint(1,10)) # adiciona 5 itens aleatorios na lista
    print('Sorteando itens')
    print('Os itens sorteados foram:', end=' ') 
    for i in numeros:
        print(i, end=' ', flush=True) # mostra os itens da lista
        sleep(1)
    print()


def somaPar(x):
    soma = 0
    for i in x: # se o numero for par ele soma
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {x}, temos {soma}')
    

def somaImpar(x):
    soma = 0
    for i in x: # se o numero for par ele soma
        if i % 2 != 0:
            soma += i
    print(f'Somando os valores impares de {x}, temos {soma}')
    

numeros = []
sorteia(numeros)
somaPar(numeros)
somaImpar(numeros)