# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO
# Início do Programa
print('\033[1;30m#\033[m' * 40)
print('\033[1;36mSEJA BEM VINDO(A) AO CALCULADOR DE MÉDIAS V1.0\033[m')
print('\033[1;30m#\033[m' * 40)
# Programa interagindo com o usuário
aluno = str(input('Digite o nome do aluno por favor: '))
n1 = float(input('Digite a nota do 1° bimestre: '))
n2 = float(input('Digite a nota do 2° bimestre: '))
n3 = float(input('Digite a nota do 3° bimestre: '))
n4 = float(input('Digite a nota do 4° bimestre: '))
# Execução das funções
media = (n1 + n2 + n3 + n4) / 4
# Respondendo ao usuário
if media >= 7.0:
    print('A média do aluno {} foi de {:.1f}. Portanto, o aluno está \033[4;32mAPROVADO!\033[m'.format(aluno, media))
elif 7 > media >= 5:
    print('A média do aluno {} foi de {:.1f}. Portanto, o aluno está em \033[4;33mRECUPERAÇÃO!\033[m'.format(aluno, media))
elif media < 5.0:
    print('A média do aluno {} foi de {:.1f}. Portanto, o aluno está \033[4;31mREPROVADO!\033[m'.format(aluno, media))
    print('\033[1;32mESTUDE MAIS!\033[m')
