from datetime import date
ano_atual = date.today().year
maior = menor = 0
for c in range(0, 7):
    c += 1
    ano = int(input('EM QUE ANO A {} PESSOA NASCEU? '.format(c)))
    idade = ano_atual - ano
    if idade > 18:
        maior += 1
    else:
        menor += 1

print('Ao todo foram {} maiores de 18 anos e {} menores de 18.'.format(maior, menor))