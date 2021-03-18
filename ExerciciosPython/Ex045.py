# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros
from random import randint
from time import sleep
# Iniciando o jogo
print('\033[1;30m°\033[m' * 30)
print('\033[1;31mPEDRA, PAPEL OU TESOURA V1.0\033[m')
print('\033[1;30m°\033[m' * 30)
# Computador seleciona algo
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
# Jogador seleciona opções
print('''Escolha uma opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[1;31mJO\033[m')
sleep(1)
print('\033[1;36mKEN\033[m')
sleep(1)
print('\033[1;37mPO!\033[m')
print('\033[1;32m*\033[m' * 25)
print('\033[1;31mComputador jogou {}\033[m'.format(itens[computador]))
print('\033[1;36mJogador jogou {}\033[m'.format(itens[jogador]))
print('\033[1;32m*\033[m' * 25)
if computador == 0:             # Computador joga PEDRA
    if jogador == 0:
        print('\033[1;33mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;36mJOGADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCE!\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:              # Computador joga PAPEL
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1;33mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;36mJOGADOR VENCE!\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('\033[1;36mJOGADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1;31mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;33mEMPATE!\033[m')
    else:
        print('JOGADA INVÁLIDA!')
else:
    print('JOGADA INVALIDA!')
