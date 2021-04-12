# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz com a formatação correta.

matriz = [[], [], []]

for c in range(0, 3):
    for x in range(0, 3):
        matriz[c].append(int(input(f'Valor [ {c}, {x} ]: ')))

print('-' * 30)

for c in range(0, 3):
    for x in range(0, 3):
        print(f'[ {matriz[c][x]} ]', end='')
    print()