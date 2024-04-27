'''
1 - > ler o nome e o peso de varias pessoas V
2 - > guardar tudo numa lista V
3 - > quantas pessoas foram cadastradas V
4 - > listagem de pessoas mais pesadas X
5 - > listagem com as pessoas mais leves X
'''
lista_vazia = []
pessoas = []
maior = 0
menor = 0
while True:
    # // lista vai adicionar itens
    lista_vazia.append(str(input('NOME: ')).strip())
    lista_vazia.append(float(input('PESO: ')))
    pessoas.append(lista_vazia[:])
    lista_vazia.clear()
    # // joga os itens em outra lista e apaga a primeira pra não duplicar os itens
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while resp not in 'SN' :
        resp = str(input('Resposta invalida. Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
    # // coisa de sempre pra continuar / parar o loop
for p, t in enumerate(pessoas):
    if pessoas[0] == t:
        maior = t[1]
        menor = t[1]
    else:
        if pessoas[p] == t and t[1] > maior:
            maior = t[1]
        if pessoas[p] == t and t[1] < menor:
            menor = t[1]  
pess_cad = len(pessoas)
print(f'O maior peso foi {maior}kg. Peso de ->', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {menor}kg. Peso de ->', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()
print(f'Foram cadastradas {pess_cad} pessoas')
print(pessoas)  