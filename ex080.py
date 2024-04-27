''' 
digitar 5 numeros e colocar numa lista
tem que digitar e automaticamente ir pra posição correta
sem usar .sort()
-> mostrar o resultado da lista ordenada

'''
lista = []
for c in range(0, 5):
    numeros = int(input('DIGITE UM NUMERO: '))
    if c == 0 or numeros > lista[-1]:
        lista.append(numeros)
        print('Foi pro ultimo lugar')
    else:
        posicao = 0
        while posicao < len(lista):
            if numeros <= lista[posicao]:
                lista.insert(posicao, numeros)
                print(f'Adicionado na posição {posicao}.')
                break
            posicao += 1
print(f'A lista foi \033[32m{lista}.\033[m')