# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
#Incio do programa
print('\033[0;36m=\033[m' * 25)
print('\033[1;33mCONVERSOR EM BINÁRIOS\033[m')
print('\033[0;36m=\033[m' * 25)
#Programa pede para usuário pedir um número
num = int(input('Digite um número inteiro por favor: '))
print('\033[1;34m*\033[m' * 30)
print('\033[1;33mEscolha uma opção para converter:\033[m \n1 para binário: \n2 para octal: \n3 para hexadecimal:\033[m')
print('\033[1;34m*\033[m' * 30)
opção = int(input('Digite sua opção por favor: '))
#Resposta do programa
if opção == 1:
    print('O número {}, em binário é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {}, em octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {}, em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA! Tente novamente.')
