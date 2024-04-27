lista = []
media = 0
while True:
    dados = {'Nome': str(input('NOME: ')).strip()}
    dados['Sexo'] = str(input('SEXO: ')).strip().upper()
    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = str(input('Entrada inválida. [M/F]: ')).strip().upper()
    dados['Idade'] = int(input('IDADE: '))
    media += dados['Idade']
    lista.append(dados.copy())
    dados.clear()
    perg = str(input('QUER CONTINUAR? [S/N]')).strip().upper()
    while perg not in 'SN':
        perg = str(input('RESPOSTA INVALIDA. TENTE NOVAMENTE. [S/N]')).strip().upper()
    if perg == 'N':
        break
media = media / len(lista)
print('-' * 30)
print(f'A média de idade do grupo foi {media:.1f}')
print(f'O grupo tem {len(lista)} pessoas.')
print(f'As mulheres cadastradas foram:', end=' ')
for ficha in lista:
    if ficha['Sexo'] in 'F':
        print(ficha['Nome'], end=' ')
print()
print('As pessoas com idade acima da média foram:')
print('-' * 30)
for ficha in lista:
    if ficha['Idade'] > media:
        print(f'Nome: {ficha['Nome']}; Sexo: {ficha['Sexo']}; Idade: {ficha['Idade']};')
print('-' * 30)