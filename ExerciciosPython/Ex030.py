# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('=' * 25)
print('IMPAR OU PAR? DESCUBRA!')
print('=' * 25)
num = int(input('Digite um número para saber ele é IMPAR ou PAR: '))
if (num % 2) == 0:
    print('Este número é PAR.')
else:
    print('Este número é IMPAR.')
