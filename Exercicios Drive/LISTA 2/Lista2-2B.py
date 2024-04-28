def soma(dic):
    valor_l = sum(dic['Lucas'])
    valor_p = sum(dic['Pedro'])
    
    if valor_l > valor_p:
        return 'Lucas'
    if valor_p > valor_l:
        return 'Pedro'
    else:
        return 'Empate'


lista = [[], []]
dic = {}
c = 1

while c < 4:
    num = input(f'Pontuação da {c}ª partida: ').split()
    if len(num) == 2:
        if 0 <= int(num[0]) <= 100 and 0 <= int(num[1]) <= 100:
            lista[0].append(int(num[0]))
            lista[1].append(int(num[1]))
            c += 1
        else:
            print('Valores Inválidos. Tente novamente.')
    else:
        print('Quantidade de valores inválida. Tente novamente.')
        
dic['Lucas'] = lista[0]
dic['Pedro'] = lista[1]

print(soma(dic))
