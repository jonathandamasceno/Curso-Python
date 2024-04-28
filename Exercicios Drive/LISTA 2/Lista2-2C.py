def confere(e, c):
    if e == c:
        return 'Soltar pacote'
    else:
        return 'Nao soltar pacote'


ent = []
coord = []

while True:
    entrega = input('Coordenadas de entrega (ex.: 5 2): ').split()
    coord_atual = input('Coordenadas atuais do drone (ex.: 3 7): ').split()
    if 1 <= int(entrega[0]) <= 1000 and 1 <= int(entrega[1]) <= 1000:
        if len(entrega) == 2 and len(coord_atual) == 2:
            ent = entrega[:]
            coord = coord_atual[:]
            break
        else:
            print('Dados insuficientes. Tente novamente')
    else:
        print('Números estão fora do esperado.')

print(f'\n{confere(ent, coord)}')
