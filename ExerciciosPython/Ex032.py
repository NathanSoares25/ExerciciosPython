# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite um ano qualquer: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
