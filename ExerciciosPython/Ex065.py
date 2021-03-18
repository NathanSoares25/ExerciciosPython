# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print('-' * 20)
print('MAIOR E MENORES VALORES V1.0')
print('-' * 20)
média = soma = quanti = maior = menor = 0
resposta = 'Ss'
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quanti += 1
    if quanti == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            num = menor
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = soma / quanti
print('Você digitou {} números e a média entre eles é de {}'.format(quanti, media))
print('O maior número é {} e o menor é {}'.format(maior, menor))
