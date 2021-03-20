# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
print('\033[1;30m=-=\033[m' * 9)
print('\033[1;31mOLÁ, SEJA BEM VINDO!\033[m')
print('\033[1;30m=-=\033[m' * 9)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
print('\033[4;35mAGUARDE...\033[m')
sleep(1.5)
while opção != 5:
    print('\033[1;30m-\033[m' * 20)
    print('Qual é a sua sua opção?')
    print('''    \033[1;31m[ 1 ] SOMAR\033[m
    \033[1;32m[ 2 ] MULTIPLICAR\033[m
    \033[1;33m[ 3 ] MAIOR NÚMERO\033[m
    \033[1;34m[ 4 ] NOVOS NÚMEROS\033[m
    \033[1;35m[ 5 ] SAIR DO PROGRAMA\033[m''')
    print('\033[1;30m-\033[m' * 20)
    opção = int(input('Digite sua opção: '))
    print('\033[4;35mAGUARDE...\033[m')
    sleep(1.5)
    if opção == 1:
        soma = n1 + n2
        print('\033[1mA soma de \033[31m{}\033[m + \033[31m{}\033[m é \033[32m{}\033[m'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('\033[1mA multiplicação entre \033[31m{}\033[m x \033[31m{}\033[m é \033[32m{}\033[m\033[m'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[1mO maior número entre \033[31m{}\033[m e \033[31m{}\033[m é \033[32m{}\033[m\033[m.'.format(n1, n2, maior))
    elif opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digte o segundo valor: '))
        print('\033[4;35mAGUARDE...\033[m')
        sleep(1.5)
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção Incorreta! Tente Novamente!')
print('Fim do programa!')
