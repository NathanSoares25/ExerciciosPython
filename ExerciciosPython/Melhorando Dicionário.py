time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez na {c + 1}º partida? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opção in 'SN':
            break
        print('     >>> ERRO! TENTE NOVAMENTE! <<<     ')
    if opção == 'N':
        break
print('-' * 40)
print('Cod. ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40 )
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('>>> ERRO! CÓDIGO INVÁLIDO! <<<')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)

print('>>> FIM <<<')
