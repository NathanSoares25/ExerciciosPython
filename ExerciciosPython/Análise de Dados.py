# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.
idade = sexo = conti = conts = contm = 0
while True:
    print('=-' * 20)
    print('\033[1;31mCADASTRO DE PESSOAS V1.0\033[m')
    print('=-' * 20)
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo? [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F]: ')).upper().strip()[0]
    print('-' * 20)
    opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    print('-' * 20)
    if idade >= 18:
        conti += 1
    if sexo in 'Mm':
        conts += 1
    if sexo in 'Ff':
        if idade <= 20:
            contm += 1
    if opção == 'N':
        break
print('---FIM DO PROGRAMA---')
print(f'Total de pessoas com \033[4;32mmais de 18 anos:\033[m {conti}')
print(f'Ao todo, tivemos {conts} homens cadastrados.')
print(f'E temos um total de {contm} mulheres com menos de 20 anos.')
