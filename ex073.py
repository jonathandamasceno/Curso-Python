times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Red Bull Bragantino',
         'Fluminense', 'Athletico', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá',
         'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print(f'Lista com todos os times: {times}')
print(f'\nPrimeiros 5 colocados: {times[0:5]}')
print(f'Ultimos 4 colocados na tabela: {times[-4:]}')
print(f'Em ordem alfabetica: {sorted(times)}')
if 'Bahia' in times:
    print(f'O bahia está na {times.index('Bahia') + 1}ª posição')
else:
    print('Bahia não está na serie a.')
'''
    metodos que eu pensei pra pegar os ultimos 4 colocados:
    
        print(times[16:20]) 
        print(times[-4:])
        
'''
