produtos = ('lapis', 1.75, 
            'caderno', 5, 
            'borracha', 1.50, 
            'estojo', 10, 
            'mochila', 25)
# listagem de itens
c = 0

while c < len(produtos):
    print(f'{produtos[c]:.<20}', end=' ') # produto na posição c (produto[0])
    c += 1  # aumenta pra [2]                                        
    print(f'R$ {produtos[c]:.2f}')        # produto na posição c (produto[1])
    c += 1  # aumenta pra [3]

'''
ou
'''
'''
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<20}', end=' ')
    else:
        print(f'R$ {produtos[c]:.2f}')
'''
# < alinhado a direita
# > alinhado a esquerda
# ^ centralizado
# uma da formas de mostrar 2 elementos numa linha (pode ser mais termos dependendo)