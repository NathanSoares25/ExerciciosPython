# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Iniciando o Programa
print('\033[30m→\033[m' * 35)
print('\033[1;35mO NÚMERO É PRIMO OU NÃO É? DESCUBRA!')
print('\033[30m←\033[m' * 35)
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1, 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é um número PRIMO!')
else:
    print('E por isso ele NÃO é um número PRIMO!')
