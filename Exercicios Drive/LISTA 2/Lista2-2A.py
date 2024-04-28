def calc(lista):
    qtd_pistas = int(lista[0])
    qtd_pessoas = int(lista[1])
    qtd_pess_pp = int(lista[2]) 
    capacidade_max = qtd_pistas * qtd_pessoas
    
    if 1 <= qtd_pistas and qtd_pessoas and qtd_pess_pp <= 100:
        if capacidade_max > qtd_pess_pp:
            return 'S'
        else:
            return 'N'
    else:
        return 'Dados invalidos. Reinicie o processo.'


lista = []
while True:
    num = input('Digite os dados. De 1 a 100: ').split()
    if len(num) == 3:
        lista = num[:]
        break
    else:
        print('Digite todos os dados corretamente.')
        
        
print(calc(lista))
