'''
1-> ler varios numeros e colcocar numa lista
2-> quantos numeros foram digitados
3-> lista de valores ordenada de forma decrescente
4-> se o valor 5 está ou não na lista
'''
lista = []
c = 0
while True:
    lista.insert(c, int(input(f'DIGITE O NUMERO DA POSIÇÃO {c}: '))) # 1)
    resp = str(input('QUER CONTINUAR? [S/N]: ')).strip().upper()
    c += 1
    while resp not in 'SN':
        resp = str(input('DIGITE UMA RESPOSTA VALIDA. [S/N]: ')).strip().upper()
    if resp == 'N':
        break  
if 5 in lista: # 4
    print(f'O numero cinco aparece {lista.count(5)} vezes.')
else:
    print(f'O numero cinco não foi digitado.')
print(f'foram digitado \33[32m{len(lista)}\33[m numeros.') # 2)
lista.sort(reverse = True) # 3.1)
print(f'a ordem decrescente é {lista}.') # 3.2)