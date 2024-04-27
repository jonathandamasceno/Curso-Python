# melhorar o 93
lista = []
jogadores = []
total = 0
while True:
    dados = {'Nome': str(input('Nome: ')).strip()}
    partidas = int(input(f'QUANTIDADE DE PARTIDAS QUE {dados['Nome']} JOGOU: '))
    for c in range(0, partidas):
        lista.append(int(input(f'QUANTOS GOLS NA PARTIDA {c+1}? ')))
    for i in lista:
        total += i
    dados['Gols'] = lista.copy()
    dados['Total'] = total
    total = 0
    lista.clear()
    jogadores.append(dados)
    resp = str(input('QUER CONTINUAR? [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Resposta Inválida. Tente novamente. [S/N]: ')).strip().upper()
    if resp in 'N':
        break
print('N° ', end='')
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for p, i in enumerate(jogadores):
    print(f'{p}  ', end ='')
    for k, v in i.items():
        print(f'{str(v):<15}', end='') 
    print()
while True:
    perg = int(input('MOSTRAR DADOS DE QUAL JOGADOR? [999 Para] '))
    print('-'*40)
    if perg == 999:
        break
    if perg > len(jogadores):
        print(f'Não exite jogador com o codigo {perg}.')
    else:
        print(f' - Levantamento do jogador {jogadores[perg]['Nome']}:')
        print('-'*40)
        for t in jogadores:
            for gf in range(0, len(jogadores[perg]['Gols'])):
                print(f' - No jogo {gf+1} fez {jogadores[perg]['Gols'][gf]} gols.')
        print('-'*40)