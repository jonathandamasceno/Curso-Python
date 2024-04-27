'''
1 - > Ler 9 valores pelo teclado
2 - > Fazer isso:
    1   |   2  |    3
    4   |   5  |    6
    7   |   8  |    9
'''
lista_vazia = []
lista = []
p = 0
s = 1
t = 2
for c in range(0 , 3):
    lista_vazia.append(int(input(f'Digite o numero da {c},{p} posição: ')))
    lista_vazia.append(int(input(f'Digite o numero da {c},{s} posição: ')))
    lista_vazia.append(int(input(f'Digite o numero da {c},{t} posição: ')))
    lista.append(lista_vazia[:])
    lista_vazia.clear()
for c in range(0,3):
    for l in range(0,3):
        print(f'[{lista[c][l]:^5}]', end='') # :^5 alinhado no meio de 5 espaços
    print()  
print('='*52)
print(f'lista completa - > \033[034m{lista}\033[m') 

# jeito iniciante
'''
print(f'| {lista[0][0]}   |   {lista[0][1]}   |   {lista[0][2]} |')
print(f'| {lista[1][0]}   |   {lista[1][1]}   |   {lista[1][2]} |')
print(f'| {lista[2][0]}   |   {lista[2][1]}   |   {lista[2][2]} |')
'''