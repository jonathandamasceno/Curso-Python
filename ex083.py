'''
1 -> digitar uma expressão matematica entre parenteses
2 -> verificar se a expressão é válida
ex.: ((a+b) * c) -> Válida
     (a+b) * c ) -> Inválida
'''
lista = []
lista.append(str(input('DIGITE UMA EXPRESSÃO: ')))
direita = []
esquerda = []
for t in lista:                              # -> pra cada termo na lista ( no caso só um)
    for  letra in t:                         # -> pra cada letra do termo
        if '(' in letra:                     # -> se tem o parentese dentro
            direita.append('(')  
        elif ')' in letra:                   # -> idem
            esquerda.append(')')
if len(direita) == 0 and len(esquerda) == 0: # se não tiver nenhum ele avisa
    print('\033[33mNão tem parenteses.\033[m')
else:   
    if len(direita) % 2 == 0 or len(esquerda) % 2 == 0: # se for 1 - par / 2 - impar, é invalida
        print('\033[31mEXPRESSÃO INVALIDA.\033[m')  
    if len(direita) % 2 != 0 and len(esquerda) % 2 != 0:# se for 1 - impar/par / 2 - impar/par, é valida
        print('\033[36mEXPRESSÃO VALIDA.\033[m')        # impar + impar = par
print(lista)                                            # par + par = par

''''
if len(direita) % 2 == 0 or len(esquerda) % 2 == 0:
    print('EXPRESSÃO INVALIDA.')  
if len(direita) % 2 != 0 and len(esquerda) % 2 != 0:
    print('EXPRESSÃO VALIDA.')
    
explicação da mentalidade desse código:

-> se o numero de parenteses for impar = nao fecha
-> se o numero de parenteses for par = fecha

se o tamanho da variavel 'direita'( ( ) ou 'esquerda' ( ) ) for par e a outra impar,
a soma daria impar, aí expressão se torna invalida, se as duas forem impares a soma dá par
fazendo ela ser válida
'''