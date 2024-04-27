def ficha(nom='<desconhecido>', gols=0):
    print(f'O jogador {nom} fez {gols} gols no campeonato.')


print('-'*30)
n = str(input('NOME: '))
g = str(input('QUANTOS GOLS FEZ: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
print('-'*30)

