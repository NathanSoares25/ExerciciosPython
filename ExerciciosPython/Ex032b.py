# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. MODO 2
from datetime import date
ano = int(input('Digite um ano qualquer. Para analisar o ano atual digite 0 '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
