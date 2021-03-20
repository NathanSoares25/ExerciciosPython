# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Inicio do Programa
from time import sleep
soma = 0
cont = 0
print('\033[1;30mSOMANDO PARES!!!!\033[m')
sleep(1)
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('\033[1;32mAGUARDE...\033[m')
sleep(1)
print('Entre os \033[4;33m6\033[m números digitados... \nExiste \033[4;33m{}\033[m números pares; \nE a soma dos pares é de \033[4;33m{}\033[m'.format(cont, soma))
