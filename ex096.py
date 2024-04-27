'''
1 - > receber dois valores -> Largura X Comprimento
2 - > Mostrar a área
3 - > usando função
'''
def area(lar, com):
    res = lar * com
    print(f'A area do terreno com especificações de largura {lar} e comprimento {com} é {res}m²')
    

l = float(input('LAGURA DO TERRENO(m): '))
c = float(input('COMPRIMENTO DO TERRENO(m): '))
area(l, c)