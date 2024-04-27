# mostrar o maior e o menor nas posições
lista = list()
for c in range(0, 5):
    lista.append(int(input(f'DIGITE O NUMERO DA POSIÇÃO {c}: ')))    
maior = max(lista)
menor = min(lista)
print(f'\nO numero {maior} aparece nas posicoes', end=' ')
for p, n in enumerate(lista):
    if n == maior:
        print(f'{p}...', end= ' ')
print(f'\nO numero {menor} aparece nas posicoes', end=' ')
for p, n in enumerate(lista):
    if n == menor:
        print(f'{p}...', end= ' ')
print(f'\nVocê digitou os valores: \33[36m{lista}\33[m') 
# qual o maior valor
print(f'o maior valor: {maior}, está na \33[32m {lista.index(maior) + 1}ª\33[m posição')
                                  # saber a posição do maior termo (primeira ocorrência)
# qual o menor valor
print(f'o menor valor: {menor}, está na \33[35m {lista.index(menor) + 1}ª\33[m posição')
                                  # saber a posição do menor termo (primeira ocorrência)