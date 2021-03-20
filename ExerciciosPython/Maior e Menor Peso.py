# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é de {}Kg.'.format(maior))
print('E o menor peso é de {}Kg.'.format(menor))
