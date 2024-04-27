dados = ['Pedro', 25] # uma lista normal
pessoas = []
pessoas.append(dados[:] )# faz uma copia de dados e coloca em outra lista
# ficaria assim -> pessoas = [['Pedro', 25], ['Maria', 35]]
dados[0] = 'Maria'
dados[1] = 32
pessoas.append(dados[:])
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[0][1])
# da pra criar direto
preco_jogos = [['Minecraft', 30], ['Pubg', 0], ['Mario Kart', 60]]
print(preco_jogos[1][0])
for t in preco_jogos:
    print(f'O jogo {t[0]}', end=' ')
    print(f'custa R${t[1]:.2f}')

# .clear() apaga os dados da lista
# tem que colocar no 'for' quando for adicionar itens pra não da erro