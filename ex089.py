'''
1 -> pegar Nome / Notas e colocar em listas
2 -> fazer uma tabela com o nome/posição/média de cada aluno
3 -> mostrar todas as notas individualmente -> 999 pra parar o loop
'''
lista_vazia = []
lista_pessoas = []
media = 0
notas = []
while True:
    lista_vazia.append(str(input('NOME: ')))
    notas.append(float(input('PRIMEIRA NOTA: ')))
    notas.append(float(input('SEGUNDA NOTA: ')))
    # dava pra fazer - > nome = // nota1 = // nota2 = // media = //
    # depois era só fazer
    # lista_pessoas.append([nome, [nota1, nota2], media])
    # diminuiria o codigo
    media = (notas[0] + notas[1]) / 2
    lista_vazia.append(media)
    lista_vazia.append(notas[:])
    lista_pessoas.append(lista_vazia[:])
    lista_vazia.clear()
    notas.clear()
    resp = str(input('QUER CONTINUAR? [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('DIGITE UMA OPÇÃO VÁLIDA [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print(f'{"Nº":<5}{"NOME":^10}{"MÉDIA":>10}') # meio de alihar a string 
print('='*30)
for pessoa in range(0, len(lista_pessoas)): # dava pra fazer com um for só usando o enumerate()
    print(f'{pessoa:<5}', end= ' ')
    for dado in range(0,2):
        print(f'{lista_pessoas[pessoa][dado]:^10}', end=' ')
    print()
print('='*30)
while True:
    escolha = int(input('De qual pessoa quer ver as notas? [999 PARA] '))
    if escolha == 999: 
        break
    if escolha <= len(lista_pessoas) - 1:
        print(f'As notas de {lista_pessoas[escolha][0]} foram: {lista_pessoas[escolha][2]}')