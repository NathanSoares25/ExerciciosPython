# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais
# Início do programa
print('\033[1;36m*\033[m' * 30)
print('\033[1;32mMAIOR OU MENOR? DESCUBRA!!!!!\033[m')
print('\033[1;36m*\033[m' * 30)
# Perguntando ao usuário
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
# Resposta do programa
if a > b:
    print('O número {} é maior que o número {}'.format(a, b))
elif b > a:
    print('O número {} é maior que o número {}'.format(b, a))
else:
    print('Não existe valor maior, pois ambos são iguais!')
