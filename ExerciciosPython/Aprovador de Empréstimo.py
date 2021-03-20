# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
# Inicio do programa.
print('\033[0;33m *' * 17)
print('\033[1;36mBEM VINDO AO EMPRESTIMO DIGITAL!')
print('\033[0;33m *\033[m' * 17)
# Perguntando o valor da casa, salário e tempo de pag.
valor = float(input('Qual é o valor da casa que você deseja comprar? R$'))
salario = float(input('Digite o seu salário por favor: R$'))
anos = int(input('Em quantos anos você deseja pagar a casa? '))
print('\033[1;30mAGUARDE POR FAVOR...\033[m')
sleep(2)
# Se as parcelas forem maior que 30% do salário do usuário
prestação = valor / (anos * 12)
minimo = salario * 30/ 100
# Programa respondendo o usuário
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('\033[4;32mO empréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[4;31mO empréstimo foi NEGADO!\033[m')
