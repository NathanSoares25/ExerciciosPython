# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
print('-' * 25)
print('RANDOMIZADOR V1.0:)')
print('-' * 25)
print('Irei pensar em um número de 0 a 5. Será que você acerta qual número eu pensei? VAMOS VER!')
num = int(input('Digite um número de 0 a 5: '))
sorteado = random.randint(0, 5)
print('PROCESSANDO...')
sleep(2)
print('Eu pensei no número {}'.format(sorteado))
if num == sorteado:
    print('PARABÉNS! Você acertou o número em que eu pensei, na proxima não irei facilitar!')
else:
    print('ERRRROOOOOUUUU! Eu venci!')
