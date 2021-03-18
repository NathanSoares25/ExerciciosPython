# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = input('Digite um número inteiro: ')
milhar = num[0]
centena = num[1]
dezena = num[2]
unidade = num[3]
print('O milhar é {}.'.format(milhar))
print('A centena é {}.'.format(centena))
print('A dezena é {}.'.format(dezena))
print('A unidade é {}.'.format(unidade))
