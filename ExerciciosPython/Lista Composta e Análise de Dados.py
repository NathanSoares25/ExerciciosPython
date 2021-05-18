# Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas
# Uma listagem com as pessoas mais leves

dados = list() # lista para pegar os dados
pessoas = list() # lista com os dados da pessoas cadastradas
pesos = list() # Lista com os pesos
cont = 0

while True:
    nome = str(input('Digite seu nome: ')) # Ler o nome do usuário
    peso = int(input('Digite seu peso: ')) # ler os peso do usuário
    dados.append(nome) # Adiciona o nome em "Dados"
    dados.append(peso)
    pesos.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0] # Opção de continuar ou não com o programa

    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0] # Enquanto usuário não digitar 'S' ou 'N' o programa ficará em looping

    if opção in 'N':
        break


print('-' * 30)
print(f'Foram cadastradas {cont} pessoas.')

print(f'O maior peso foi [{max(pesos)}]Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == max(pesos): # Verifica qual é o maior peso.
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {min(pesos)}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == min(pesos): # Verifica qual é o menor peso
        print(f'[{p[0]}]', end=' ')


