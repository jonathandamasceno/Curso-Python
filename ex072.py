num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
        'sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
cont = 'S'
while True:
    escolha = int(input('ESCREVA UM NUMERO DE 0 A 20: '))
    while escolha < 0 or escolha > 20: # verifica se foi digitado a range correto.
        escolha = int(input('ESCREVA UM NUMERO VALIDO ENTRE 0 E 20: '))
    print(f'O numero digitado foi {num[escolha]}.')# tupla[posição]
    cont = str(input('quer continuar? [S/N]: ')).upper().strip() # se continua o programa ou não.
    while cont not in 'SN': # se não for digitado 'S' ou 'N' ele repete a pergunta.
        cont = str(input('Digite um valor válido. [S/N]: ')).upper().strip()
    if cont == 'N': # resposta sendo "N", ele para.
        break
print('fim')



