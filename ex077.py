# identificar as vogais nas palavras selecionadas
comida = ('Hamburguer', 'Batata frita', 'Coca Cola', 'Salgadinho', 'Sorvete', 'Abacaxi')
vogais = ('a', 'e', 'i', 'o', 'u') 

for com in comida:                                      #para cada comida dentro da tupla
    print(f'\nNa comida {com} tem as vogais: ', end='') #printa o nome da comida
    for letra in com:                                   #para cada letra dentro da outra tupla 
        if letra.lower() in vogais:                     #se ela estiver dentro 
            print(letra.lower(), end=' ')               #escreve qual é 
                                                        #.lower() pra testar mesmo se for maiuscula
                                                        #pode ser -> if letra.lower() in 'aeiou':