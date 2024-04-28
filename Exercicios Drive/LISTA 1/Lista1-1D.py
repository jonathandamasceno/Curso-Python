# soma os valores e multiplica por 3

def saida(l1, l2):
    soma1 = sum(l1)
    soma2 = sum(l2)
    
    res = soma1 - (soma2 * 3)
    return res

c = 0
lista1 = []
lista2 = []
while c <= 2:
    ovos = int(input('Digite três numeros (de 6 a 20): '))
    if 6 <= ovos <= 20:
        lista1.append(ovos)
        c += 1 
    else:
        print('Digite os dados corretamente.')
c = 0        
while c <= 2:
    ovos_env = int(input('Digite três numeros (de 0 a 2): '))
    if 0 <= ovos_env <= 2:
        lista2.append(ovos_env)
        c += 1 
    else:
        print('Digite os dados corretamente.')
        

print(saida(lista1, lista2))
