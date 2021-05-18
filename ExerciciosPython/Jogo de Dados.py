# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque em ordem, sabendo que vencedor tirou o maior número no dado

# Importando bibliotecas
from random import randint
from time import sleep
from operator import itemgetter

# Dicionário com os jogadores e com o randomizador de 1 a 6
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}

# Criei uma lista de ranking dos jogadores
rank = []

print('>>> SORTEANDO VALORES <<<')
for c, v in jogadores.items():
    print(f'{c} tirou o número {v} no dado. ')
    sleep(1)

# Criando o ranking dos jogadores
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-' * 20)
print('   >>> RANKING DOS JOGADORES <<<   ')
print('-' * 20)
for i, v in enumerate(rank):
    print(f'O {i + 1}º lugar foi do {v[0]} com {v[1]} pontos.')
    sleep(1)
