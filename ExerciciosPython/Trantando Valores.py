# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
from time import sleep
print('-' * 20)
print('TRATANDO VALORES V1.0')
print('-' * 20)
print('INCIANDO, AGUARDE...')
sleep(1.5)
soma = cont = num = 0
num = int(input('Digite um valor [digite 999 para parar.]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor [digite 999 para parar]: '))
print('Você digitou {} números e a soma deles é igual a {}'.format(cont, soma))
