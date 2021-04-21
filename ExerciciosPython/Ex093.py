# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Criando dicionario com dados do jogador e uma lista de gols
dadosjogador = dict()
gols = list()
totalgol = 0

# Interação com o usuário
dadosjogador['Nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas {dadosjogador["Nome"]} jogou?  '))

#criando um for para repetir o total de vezes que o usuário digitou acima
for c in range(0, partidas):
    p = int(input(f'Quantos gols {dadosjogador["Nome"]} fez na {c + 1}º partida? '))
    gols.append(p)
    totalgol += 1

dadosjogador['Gols'] = gols
dadosjogador['Total de Gols'] = totalgol

print('*' * 40)
print(dadosjogador)
print('*' * 40)

for k, v in dadosjogador.items():
    print(f'O campo {k} tem valor {v}.')
print('*' * 40)
print(f'O jogador {dadosjogador["Nome"]} jogou {partidas} partidas.')

for c in range(0, partidas):
    print(f'Na partida {c + 1} ele fez {gols[c]} gols')
print(f'Foi um total de {totalgol} gols! ')

# CORREÇÃO DO GUANABARA

jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez na {c + 1}º partida? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-' * 40)
print(jogador)
print('-' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-' * 40)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols')