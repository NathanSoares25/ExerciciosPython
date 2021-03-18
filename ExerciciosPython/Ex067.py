# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('-' * 20)
print('TABUADA V3.0')
print('-' * 20)
n = 0
cont = -1
while True:
    n = int(input('Digite o valor para verificar a tabuada: '))
    if n <= cont:
        break
    print('-' * 20)
    print(f'{n} x {0} = {n * 0}')
    print(f'{n} x {1} = {n * 1}')
    print(f'{n} x {2} = {n * 2}')
    print(f'{n} x {3} = {n * 3}')
    print(f'{n} x {4} = {n * 4}')
    print(f'{n} x {5} = {n * 5}')
    print(f'{n} x {6} = {n * 6}')
    print(f'{n} x {7} = {n * 7}')
    print(f'{n} x {8} = {n * 8}')
    print(f'{n} x {9} = {n * 9}')
    print(f'{n} x {10} = {n * 10}')
    print('-' * 20)
print('TABUADA ENCERRADA. Fim do programa!')

# CORREÇÃO DO EXERCÍCIO

'''while True:
    n = int(input('Digite um valor para verificar a tabuada: '))
    if n <= 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('TABUADA ENCERRADA. Fim do programa!')'''
