'''
1 -> ler varios numeros e colocar numa lista
2 -> criar duas listas extras, uma com os pares e outra com os impares
3 -> mostrar todas as 3 listas
'''
lista1 = []
lista_par = []                                                                  # 2
lista_impar = []                                                                # 2
c = 0
while True:
    lista1.insert(c, int(input(f'DIGITE O TERMO DA POSIÇÃO {c}: ')))            # 1
    if lista1[c] % 2 == 0:
        lista_par.insert(c, lista1[c])
    if lista1[c] % 2 != 0:
        lista_impar.insert(c, lista1[c])
    resp = str(input('QUER CONTINUAR? [S/N]: ')).strip().upper()
    c += 1
    while resp not in 'SN':
        resp = str(input('Digite uma resposta valida. [S/N]: ')).strip().upper()
    if resp == 'N':
        break
 
print(f'Os valores da primeira lista foram \33[35m{lista1}\33[m.')              # 3
print(f'Os valores da lista só com pares foram \33[36m{lista_par}\33[m.')      # 3
print(f'Os valores da lista só com pares foram \33[32m{lista_impar}\33[m.')     # 3

'''
outro jeito que dá pra fazer ( adicionando os valores depois de completar a lista1)

c = 0 
for itens in lista1:
    if itens % 2 == 0:
        lista_par.insert(c, lista1[c])
    else: 
        lista_impar.insert(c, lista1[c])
    c += 1
print(lista_par)
print(lista_impar)

-> eu fiz adicionando durante
'''