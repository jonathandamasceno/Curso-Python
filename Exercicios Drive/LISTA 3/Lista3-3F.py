# numero primo
# dividido só por ele mesmo e por 1
ver = 0
lista = []
while True:
    numeros = input('Digite os numeros: ').split()
    try:
        ini = int(numeros[0])
        fim = int(numeros[1])
        while ini <= fim:
            for i in range(1, fim+1):
                if ini % i == 0:
                    ver += 1
            if 1 <= ver <= 2:
                lista.append(ini)
            ini += 1
            ver = 0
        print(len(lista))
    except IndexError:
        print('digite os dados novamente')
    else:
        break
print('-' * 60)
print(lista)   
