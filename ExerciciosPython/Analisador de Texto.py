# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# – O nome com todas as letras maiúsculas e minúsculas.
#
# – Quantas letras ao todo (sem considerar espaços).
#
# – Quantas letras tem o primeiro nome.
nome = str(input('Olá, Digite seu nome completo: '))
print('Analisando o seu nome...')
print('O nome {} em MAIÚSCULO ficará {}.'.format(nome, nome.upper()))
print('O nome {} em minúsculo ficará {}.'.format(nome, nome.lower()))
str(print('O nome {} tem {} letras sem contar os espaços.'.format(nome, len(''.join(nome.split())))))
str(print('O primeiro nome contém {} letras.'.format(len(nome.strip().split()[0]))))
