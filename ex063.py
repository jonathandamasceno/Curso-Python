qtd_termos = int(input('QUANTOS TERMOS QUER MOSTRAR? '))
antecessor = 0 
sucessor = 1
c = 0
while c < qtd_termos:
    c += 1
    print(sucessor, end=' -> ')
    antecessor = sucessor - antecessor
    sucessor = sucessor + antecessor
print('Fim.')