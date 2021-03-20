# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('\033[1;30m=\033[m' * 25)
print('\033[1;35mTERMOS DE PA V2.0\033[m')
print('\033[1;30m=\033[m' * 25)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = n
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')
