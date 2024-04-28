def verify(forca):
    p_max = 110
    if sum(forca) > p_max:
        return 'Hum, parece que houve um erro'
    else:
        if sum(forca) <= p_max * 0.5:
            return 'Seu pokemon nao fara progresso em batalhas'
        elif sum(forca) <= p_max * 0.66:
            return 'Seu pokemon esta acima da media'
        elif sum(forca) <= p_max * 0.79:
            return 'Seu pokemon certamente me chamou atencao'
        elif sum(forca) <= p_max * 1:
            return 'Seu pokemon e uma maravilha'


lista = []
while True:
    maxi = 0
    lista.clear()
    valores = input('Digite os atributos do pokemon: ').split()
    if len(valores) != 3:
        print('Dados digitados são inválidos')
    else:
        for i in valores:
            if 0 <= int(i) <= 40:
                lista.append(int(i))
                maxi += 0
            else:
                maxi += 1
    if maxi == 0:
        break
    else:
        print('Valores passam do limite. Tente novamente.')

print(verify(lista))
