#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[], [], []]
somapar = maiorlinha2 = somacol = 0

for c in range(0, 3):
    for x in range(0, 3):
        matriz[c].append(int(input(f'Valor [{c}, {x}]: '))) # Usuário digita os valores para colocar na matriz

print('-=' * 30)

for c in range(0, 3):
    for x in range(0, 3):
        print(f'[{matriz[c][x]}]', end='')
        if matriz[c][x] % 2 == 0:
            somapar += matriz[c][x]
    print()

print('-=' * 30)

print(f' a soma dos pares é de {somapar}.')

for x in range(0, 3):
    somacol += matriz[x][2]
print(f'A soma dos valores da terceira coluna é {somacol}.')

for c in range(0, 3):
    if c == 0:
        maiorlinha2 = matriz[1][c]
    elif matriz[1][c] > maiorlinha2:
        maiorlinha2 = matriz[1][c]
print(f'O maior valor da segunda linha é {maiorlinha2}')
