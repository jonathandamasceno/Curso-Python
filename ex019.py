from random import choice
pri_aluno = str(input('NOME DO PRIMEIRO ALUNO: '))
seg_aluno = str(input('NOME DO SEGUNDO ALUNO: '))
ter_aluno = str(input('NOME DO TERCEIRO ALUNO: '))
qua_aluno = str(input('NOME DO QUARTO ALUNO: '))
alunos = [pri_aluno, seg_aluno, ter_aluno, qua_aluno]
print('o(a) escolhido(a) foi {}'.format(choice(alunos)))