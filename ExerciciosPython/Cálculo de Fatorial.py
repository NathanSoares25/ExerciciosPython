# Faça um programa que leia um número qualquer e mostre o seu fatorial.
from time import sleep
from math import factorial
print('-' * 20)
print('FATORANDO NÚMEROS')
print('-' * 20)
print('INCIANDO...')
sleep(1.5)
n = int(input('Digite um número para saber seu fatoral: '))
c = n
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(factorial(n)))
