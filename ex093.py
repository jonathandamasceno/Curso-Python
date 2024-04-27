totgols = 0
lista = []
dados = {'Nome': str(input('NOME: ')).strip()}
partidas = int(input('Partidas Jogadas: '))
print('-'*30)
for c in range(0, partidas):
    lista.append(int(input(f'Gols marcados na partida {c+1}: ')))
for i in lista: # dava pra usar sum(lista)
    totgols += i
dados['Gols'] = lista.copy()
dados['Total'] = totgols
print('-'*30)
print(dados)
print('-'*30)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-'*30)
print(f'O jogador {dados["Nome"]} jogou {partidas} jogos.')
for i, v in enumerate(lista):
    print(f' - Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {totgols} gols.')
print('-'*30)