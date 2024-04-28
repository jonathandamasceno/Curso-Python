def calc(km, pedagio):
    tot = 0
    ini = int(pedagio[1])
    fim = int(km[1])
    passo = int(pedagio[1])
    for c in range(ini, fim + 1, passo):
        tot += c
    return tot
    
def taxa(km, pedagio):
    valor_km = int(km[0]) * int(pedagio[0])
    valor_ped = valor_km + calc(km, pedagio)
    return valor_ped


td = []
vp = []
cont = 0
while True:
    while cont == 0:
        numeros = input('Digite dois numeros: ').split()
        if 2 > len(numeros) < 2:
            print('Tente novamente')
        else:
            td = numeros[:]
            cont = 1
    while cont == 1:
        numeros = input('Digite dois numeros: ').split()
        if 2 > len(numeros) < 2:
            print('Tente novamente')
        else:
            vp = numeros[:]
            cont = 2
    if cont == 2:
        break
    
print(taxa(td, vp))
