# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=-' * 20)
print('CAIXA ELETRÔNICO NTH')
print('=-' * 20)
while True:
    opção = '0'
    valor = int(input('Digite o valor a ser sacado: R$'))
    real50 = valor // 50
    real20 = (valor - real50 * 50) // 20
    real10 = (valor - real50 * 50 - real20 * 20) // 10
    real1 = real5 = (valor - real50 * 50 - real20 * 20 - real10 * 10)
    if real50 != 0:
        print(f'Total de notas de R$50: {real50}')
    if real20 != 0:
        print(f'Total de notas de R$20: {real20}')
    if real10 != 0:
        print(f'Total de notas de R$10: {real10}')
    if real1 != 0:
        print(f'Total de notas de R$1: {real1}')
    while opção != 'S' and opção != 'N':
        opção = str(input('Deseja realizar mais um saque? [S/N]')).upper().strip()[0]
    if opção == 'N':
        break
print('-' * 20)
print('OBRIGADO E VOLTE SEMPRE AO CAIXA ELETRÔNICO NTH!!!')
print('-' * 20)
