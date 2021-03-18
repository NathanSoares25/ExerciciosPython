# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER
import datetime
# Início do programa
print('\033[1;30m@\033[m' * 32)
print('\033[1;33mCLASSIFICANDO ATLETAS DE NATAÇÃO\033[m')
print('\033[1;30m@\033[m' * 32)
# Programa interagindo com o usuário
nome = str(input('Digite o nome do atleta por favor: '))
nascimento = int(input('Digite ao ano de nascimento do atleta: '))
# Programa realizando as funções
hoje = int(datetime.date.today().year)
idade = hoje - nascimento
# Programa respondendo ao usuário
if idade <= 9:
    print('O atleta {} tem {} anos e é considerado \033[1;36mMIRIM.\033[m'.format(nome, idade))
elif idade in (9, 10, 11, 12, 13, 14):
    print('O atleta {} tem {} anos e é considerado \033[1;35mINFANTIL.\033[m'.format(nome, idade))
elif idade in (15, 16, 17, 18, 19):
    print('O atleta {} tem {} anos e é considerado \033[1;32mJUNIOR.\033[m'.format(nome, idade))
elif idade in (20, 21, 22, 23, 24, 25):
    print('O atleta {} tem {} anos e é considerado \033[1;34mSÊNIOR.\033[m'.format(nome, idade))
else:
    print('O atleta {} tem {} anos e é considerado \033[1;31mMASTER.\033[m'.format(nome, idade))


