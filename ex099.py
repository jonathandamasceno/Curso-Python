from time import sleep 
def maior(*valores):
    print('='*60)
    print('Analisando valores passados...')
    if len(valores) >= 1:
        for i in valores:
            print(f'{i}', end=' ', flush=True)
            sleep(1)
        print(f'foram informados {len(valores)} valores')
        print(f'O maior valor foi {max(valores)}')
        print('='*60)
    else:
        print('foram informados 0 valores')
        print('O maior valor foi 0')
        print('='*60)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
