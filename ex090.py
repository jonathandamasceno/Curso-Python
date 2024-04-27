dados = {}
dados['Nome'] = str(input('NOME: '))
dados['Média'] = float(input(f'MÉDIA DE {dados['Nome']}: '))
if dados['Média'] < 5:
    dados['Situação'] = 'Reprovado'
elif dados['Média'] < 7:
    dados['Situação'] = 'Em recuperação'
else:
    dados['Situação'] = 'Aprovado'
print('-'*30)
for k, v in dados.items():
    print(f'{k}: {v}')