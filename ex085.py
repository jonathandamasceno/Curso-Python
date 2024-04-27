'''
1 -> Digitar 7 numeros V 
2 -> Separar pares e impares em duas listas V 
3 -> Colocar tudo numa lista -> Lista geral[ [pares], [impares] ] V 
4 -> Mostrar em ordem crescente / (as listas separadas) V 
'''
lista_geral = []                                    # dá pra fazer lista_geral = [ [], [] ]
lista_geral.append(list())
lista_geral.append(list())
for c in range(0, 7):                               # 1
    num = int(input(f'DIGITE O {c+1}° TERMO: '))
    if num % 2 == 0:                                # 2
        lista_geral[0].insert(c, num)
        lista_geral[0].sort()                       #3
    else:
        lista_geral[1].insert(c, num)
        lista_geral[1].sort()
print(f'Todos os numeros digitados \033[036m{lista_geral}\033[m.')
print(f'Os valores pares foram \033[035m{lista_geral[0]}\033[m.')
print(f'Os valores impares foram \033[032m{lista_geral[1]}\033[m.')