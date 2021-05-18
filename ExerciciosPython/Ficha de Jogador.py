def ficha(jogador='<DESCONHECIDO>', gol=0):
    print(f'O jogardor {jogador} fez {gol} gol(s)')


nome = str(input('Digite o nome do jogador: '))
gols = str(input(f'Digite o número de gols feito por {nome}: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
