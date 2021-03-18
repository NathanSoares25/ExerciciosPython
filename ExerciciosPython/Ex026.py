# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase: ')
print('A letra', 'A', 'aparece {} vezes.'.format(frase.lower().count('a')))
print('Ela aparece pela primeira vez na posição {}.'.format(frase.lower().strip().find('a') + 1))
print('A ultima letra', 'A', 'aparece na posição {}.'.format(frase.lower().strip().rfind('a') + 1))
