# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. MODO 2
num = int(input('Digite um número:'))
print('Analisando o número...')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade é: {}'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('O milhar é: {}'.format(m))
