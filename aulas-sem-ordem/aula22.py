from func import numeros  # importando as minhas funções de outro arquivo
# func -> pacote geral
# numeros -> pacote especifico dentro de func

num = int(input('Digite um numero: '))
fat = numeros.fatorial(num)  # para usar cada uma
qua = numeros.quadrado(num)
cub = numeros.cubo(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O quadrado de {num} é {qua}.')
print(f'O cubo de {num} é {cub}.')
