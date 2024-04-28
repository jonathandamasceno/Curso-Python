def analise(lis):   
    for i in lis:
        if i['Sat. San'] < 90:
            i['Sit'] = 'Internar'
        else:
            i['Sit'] = 'Alta'
        print(i['Nome'], i['Sit'])   

    
lista = []
while True:
    entrada = input('Dados: ').upper().split()
    try:
        
        if entrada[0] == '#' and int(entrada[1]) == 0:
            break
        if 1 <= int(entrada[1]) <= 100:
            dic = {'Nome': entrada[0][0], 'Sat. San': int(entrada[1])} 
            lista.append(dic)
        else:
            print('Digite os dados corretamente.')
            
    except IndexError:
        print('Dados digitados são inválidos.')

analise(lista)
