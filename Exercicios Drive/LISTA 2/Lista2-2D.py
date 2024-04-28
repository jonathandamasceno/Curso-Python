def dividir(num):
    dic = {'Chapéuzinho Vermelho': 0, 'Vó': 0, 'Lobo': 0}
    while True:
        if num != 0:
            dic['Chapéuzinho Vermelho'] += 1
            num -= 1
        if num != 0:
            dic['Vó'] += 1
            num -= 1
        if num != 0:
            dic['Lobo'] += 1
            num -= 1
        if num == 0:
            break
    for k, v in dic.items():
        print(f'{k} {v}')


while True:
    qtd_doces = int(input('Quantidade total ( de 1 a 100 ): '))
    if 1 <= qtd_doces <= 100:
        dividir(qtd_doces)
        break
    else:
        print('O número escolhido é menor ou excede o limite. Tente novamente.')
