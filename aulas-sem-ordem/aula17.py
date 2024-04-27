# listas []
# listas podem ser mudadas
lista = [5, 2, 3, 4, 5]
# lista[1] = 'impressora'          # posso alterar
# lista.append('placa de video')   # adicionar item no final .append()
# da pra colocar input dentro do append

#lista.insert(0, 'memoria ram') # adiciona um item na posição 0 sem tirar nenhum
'''
meios de remover itens
lista.remove('mouse')
se tiver 2 termos iguais = 1, 1, 2 // o .remove() tira a primeira ocorrência
del lista[2]

lista.pop(2)
metodo '.pop()' sozinho elimina o ultimo termo

''' 
valores = list(range(0, 11)) # vai adicionar de 1 a 10 numa lista
# se estiver fora de ordem, pode usar valores.sort() pra organizar 
# da pra colocar ao contrario usando .sort(reverse=True)

for p, v in enumerate(lista):
    print(f'O valor {v} está na posição {p}')
print(valores)
print(lista)
# colocar uma lista em outra == listaB = listaA[:]


