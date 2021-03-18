# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
atual = datetime.date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    idade = atual - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Temos {} pessoas que são maior de idade.'.format(maior))
print('E também temos {} pessoas que são menor de idade.'.format(menor))
