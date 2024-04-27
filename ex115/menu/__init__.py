import cadastro as cad

# menu inteiro
def escolha():
    print('-' * 40)
    print(f'{'MENU PRINCIPAL':^40}')
    print('-' * 40)
    print('1 - \033[96mVer Pessoas Cadastradas\033[m\n2 - \033[96mCadastrar Nova pessoa\033[m\n3 - \033[96mSair do Sistema\033[m')
    print('-' * 40)
    while True: # opções
        try:
            opcao = int(input('\033[95mSua opção: \033[m'))
        except (ValueError, TypeError):
            print("Opção inválida.")
        else:
            if opcao == 1:
                try:
                    arq = open("dados.txt")
                    arq.close()
                except FileNotFoundError:
                    print('O arquivo não existe.')
                else:
                    with open("dados.txt", "r", encoding="utf-8") as dados:
                        print('-' * 40)
                        for l in dados.readlines():
                            print(l, end='')
                        print('-' * 40)
            elif opcao == 2:
                return cad.Cadastro()
            elif opcao == 3:
                print('-> Saindo...')
                break
            else:
                print('Digite um valor válido.')
    