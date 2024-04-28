def clone(numero):
    lista = []
    m = 1
    while m <= numero:
        lista.append(m)
        m *= 2
    if numero in lista:
        return 'Dattebayo'
    else:
        return 'Tururuu'
# tem q estar na potencia de 2
while True:
    try:
        num = int(input('Digite um numero: '))
    except ValueError:
        print("Digite um número.")
    else:
        break
print(clone(num))
