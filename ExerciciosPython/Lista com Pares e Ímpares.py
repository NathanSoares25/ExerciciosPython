# Crie um programa onde o usuário possa digitar 7 valores números e cadastre-os em uma lista única
# Que mantenha os valores pares e impares. No final mostre os valores pares e impares em ordem crescente

lista = list()

for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    lista.append(num) # Adiciona "num" em lista
    lista.sort() # coloca a lista em ordem crescente
    
print(f'Os números pares digitados foram: ', end='')
for p in lista: # Para cada par em lista
    if p % 2 == 0:
        print(f'{p}', end=', ')

print(f'\nOs números ímpares digitados foram: ', end='')
for i in lista: # Para cada ímpar em lista
    if i % 2 == 1:
        print(f'{i}', end=', ')
