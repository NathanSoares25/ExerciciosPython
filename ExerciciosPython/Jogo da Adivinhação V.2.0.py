# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
computador = randint(0, 10)
print('\033[1;30m=\033[m' * 20)
print('\033[1;31mRANDOMIZADOR V2.0\033[m')
print('\033[1;30m=\033[m' * 20)
print('INICIANDO...')
sleep(1.5)
print('Irei pensar em um número de \033[1;32m0\033[m a \033[1;32m10\033[m. Tente acertar o número que eu adivinhei.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite um número de \033[1;32m0\033[m a \033[1;32m10\033[m: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print('\033[1;35mPARABÉNS! VOCÊ ACERTOU!\033[m')
print('Você precisou de \033[1;30m{}\033[m tentativas para me ganhar.'.format(palpites))
