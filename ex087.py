'''
1 - soma dos valores pares 
2 - soma dos valores da 3ª coluna
3 - maior valor da 2ª linha
'''
lista_vazia = []
lista = []
p = 0
s = 1
t = 2
soma_par = soma_col = 0

for c in range(0 , 3):
    lista_vazia.append(int(input(f'Digite o numero da {c},{p} posição: ')))
    lista_vazia.append(int(input(f'Digite o numero da {c},{s} posição: ')))
    lista_vazia.append(int(input(f'Digite o numero da {c},{t} posição: ')))
    lista.append(lista_vazia[:])
    lista_vazia.clear()
print('='*52)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{lista[c][l]:^5}]', end='') # :^5 alinhado no meio de 5 espaços
    print()  
print('='*52)
print(f'lista completa - > \033[034m{lista}\033[m')
for l in range(0,3):                                            #3
    c = 1                                                       #3
    if l == 0:                                                  #3
        maior = menor = lista[c][l]                             #3
    else:                                                       #3
        if lista[c][l] > maior:                                 #3
            maior = lista[c][l]                                 #3
        if lista[c][l] < menor:                                 #3
            menor = lista[c][l]                                 #3
            
print('O maior valor da segunda linha foi {} e o menor foi {}'.format(maior, menor))
for c in range(0, 3):                                           #2
    soma_col += lista[c][2]                                     #2
print('A soma dos valores da terceira coluna foi {}'.format(soma_col))                                                 
for c in range(0,3):                                            #1
    for l in range(0,3):                                        #1
        if lista[c][l] % 2 == 0:                                #1
            soma_par += lista[c][l]                             #1
print('A soma dos numeros pares é {}'.format(soma_par))       