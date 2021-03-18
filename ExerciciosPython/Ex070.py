# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.
print('=-' * 20)
print('LOJINHA DO NATHAN')
print('=-' * 20)
prod = valor = total = contmil = cont = menorprod = 0
barato = '0'
while True:
    prod = str(input('Digite o nome do produto: '))
    valor = float(input('Qual o valor do produto? R$'))
    opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    print('-' * 20)
    total += valor
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if valor > 1000:
        contmil += 1
    if cont == 0:
        barato = prod
        menorprod = valor
        cont = 1
    else:
        if valor < menorprod:
            menorprod = valor
            barato = prod
    if opção == 'N':
        break
print('FIM DO PROGRAMA')
print('-' * 20)
print(f'A soma dos produtos foi de R${total:.2f}.')
print(f'Você tem {cont} produtos que custam mais de R$1000,00.')
print(f'O produto mais barato foi {barato} e ele custa R${menorprod:.2f}')
