# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes
from time import sleep
# Inicio do Programa
print('\033[1;30m-\033[m' * 30)
print('\033[1;36mANALISADOR DE TRIÂNGULOS V2.0')
print('\033[1;30m-\033[m' * 30)
print('O programa obteve uma atualização e agora é possível ver se o triângulo é ESCALENO, ISÓSCELES OU EQUILÁTERO')
print('Vamos conferir!')
print('Aguarde a inicialização...')
sleep(2)
# Programa interage com o usuário
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
# Programa respondendo ao usuário
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estes valores PODEM FORMAR um triângulo!')
    if r1 == r2 == r3:
        print('E estes valores formam um triângulo \033[4;33mEQUILÁTERO!\033[m')
    elif r1 != r2 != r3 != r1:
        print('E estes valores formam um triângulo \033[4;31mESCALENO!\033[m')
    else:
        print('E estes valores formam um triângulo \033[4;32mISÓSCELES\033[m')
else:
    print('Estes valores NÃO FORMAM um triângulo!')
