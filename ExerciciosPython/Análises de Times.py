# Crie um programa que mostre os 5 primeiros, os ultimos 4 colocados, todos os times em ordem alfabetica e qual time está na oitava posição
times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Athlético-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco',
         'Goiás', 'Coritiba', 'Botafogo')
pos = 0
pos8 = 8
print('=' * 100)
print(f'Os 5 primeiros são: {times[pos:5]}')
print('=' * 100)
print(f'Os 4 últimos colocados são: {times[pos-4:]}')
print('=' * 100)
print(f'Times em ordem alfabética {sorted(times)}')
print('=' * 100)
print(f'O Santos está na {pos8}º posição.')
print('=' * 100)
