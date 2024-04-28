def golounao(x, y):
    defesa = x
    ataque = y
    
    if defesa[0] != ataque[0]:
        print('Bloqueado') 
    else:
        if defesa[0] == ataque[0]:
            print('Driblado') 
            if defesa[1] == ataque[1]:
                print('Gol') 
            else:
                print('...e o goleiro pega') 


defe = []
ataq = []

while True:
    defe = str(input('Digite os dados [defesa]: ')).lower().split()
    ataq = str(input('Digite os dados [ataque]: ')).lower().split()
    if 0 >= len(defe) >= 3 or 0 >= len(ataq) >= 3:
        print('Dados inválidos')
    else:
        defe = defe[:]
        ataq = ataq[:]
        break   

golounao(defe, ataq)