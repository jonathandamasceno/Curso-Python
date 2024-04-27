from datetime import date
from time import sleep
dados = {'Nome': str(input('Nome: ')).strip(),
         'Idade': int(input('Ano de nascimento: ')),
         'ctps': int(input('Carteira de Trabalho [0 = Não tem]: ')) 
}   
if dados['ctps'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: ')) 
    dados['Salário'] = float(input('Salário: ')) 
    dados['Aposentadoria'] =  (dados['Ano de Contratação'] - dados['Idade']) + 35
    dados['Idade'] = date.today().year - dados['Idade']
else:
    dados['Idade'] = date.today().year - dados['Idade']
print('-' * 30)
for k, v in dados.items():
    print(f'{k}: {v}')
    sleep(1)
print('-' * 30)