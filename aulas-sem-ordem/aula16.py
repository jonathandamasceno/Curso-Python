variavel = (9, 8, 6, 7) 
variavel_2 = (2, 1 , 4, 3) # variavel composta usando tupla
print(f'primeira variavel {variavel}')
print(f'segunda variavel {variavel_2}')
print(f'quantidade de termos 2 variavel {len(variavel_2)}')
print('Cada termo da variavel um por um - >')

# pode ter strings e numeros numa unica tupla
# da pra juntar tuplas
variavel_3 = variavel + variavel_2
print(variavel_3)
print(variavel_3.index(9)) # vai mostrar a posição do termo, mostrando só a primeira vez que aparece
# (como se fosse um .find) 
#se fizer .index(9, 1) = vai procurar o numero nove a partir da posição [1]


# isso organiza a tupla em ordem alfabetica ou numerica
print(sorted(variavel_2))

for c in variavel_2:
    print(c)#vai escrever cada termo da tupla um por um 

'''
ou
for c in range(0, len(variavel_2)):
    print(c, end=' ')
'''  
  
'''
for c in range(0, len(lanche)):
    print(lanche[c], end=' ') # lanche na posicão c
'''

'''
for pos, c in enumerate(variavel_2):
    print(c , pos)

-> escreve tanto a posição na tupla quanto o nome do objeto
''' 

# variavel_2 pode ser chamada usando variavel_2[#] 
# # de 0 até 3 (nesse caso)
# tuplas são imutaveis
# () = tupla;
# [] = lista;
# {} = dicionario.

'''
apagando a tupla = del(variavel)
''' 