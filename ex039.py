from datetime import date
ano_nasc = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
ano_atual = date.today().year
idade =  ano_atual - ano_nasc
print('VOCE NASCEU EM {} E TEM {} ANOS EM {}'.format(ano_nasc, idade, ano_atual))
if idade > 18:
    print('JA DEVERIA TER SE ALISTADO A {} ANOS'.format(idade-18))
    print('SEU ALISTAMENTO FOI EM {}'.format(ano_atual - (idade-18)))
elif idade < 18:
    print('VOCÊ AINDA VAI SE ALISTAR, FALTAM {} ANOS.'.format(18 - idade))
