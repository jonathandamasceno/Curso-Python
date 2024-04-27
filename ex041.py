from datetime import date
ano = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
idade = date.today().year - ano
if idade <= 9:
    print('VOCÊ SE ENCAIXA NA CATEGORIA MIRIM')
elif idade < 14:
    print('VOCÊ SE ENCAIXA NA CATEGORIA INFANTIL')
elif idade < 19:
    print('VOCÊ SE ENCAIXA NA CATEGORIA JUNIOR')
elif idade < 25:
    print('VOCÊ SE ENCAIXA NA CATEGORIA SENIOR')
else:
    print('VOCÊ SE ENCAIXA NA CATEGORIA MASTER')
print(idade)