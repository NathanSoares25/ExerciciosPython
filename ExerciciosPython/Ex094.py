# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

from time import sleep

# Dicionario e lista criados
dicionario = dict()
dados = list()
idade = list()
mulheres = list()

# Contador
cont = 0

while True:
    dicionario['Nome'] = str(input('Digite seu nome: ')) # Inserindo o nome do usuário
    cont += 1 # Contador de pessoas
    dicionario['Sexo'] = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0] # Sexo do usuário

    while dicionario['Sexo'] not in 'MF': # Enquanto o sexo não for 'M' ou 'F' o programa vai ficar em looping
        print(' >>> ERRO! TENTE NOVAMENTE! <<<')
        dicionario['Sexo'] = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

    if dicionario['Sexo'] in 'Ff': # Se o sexo dentro do dicionario for feminino
        mulheres.append(dicionario['Nome']) # adicionando as mulheres em uma lista

    dicionario['Idade'] = int(input('Digite sua idade: ')) # Idade do usuário
    idade.append(dicionario['Idade']) # colocando as idades do dicionario dentro de uma lista

    dados.append(dicionario.copy()) # Adicionei os todos os dados do dicionario dentro de uma lista

    opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]  # Opção de escolha para continuar ou para o programa

    while opção not in 'SN':  # Enquanto a opção for diferente de sim ou não, o programa continuará perguntando
        print('   >>> OPÇÃO INCORRETA <<<   ')
        opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    if opção == 'N':  # Se o usuário digitar 'N' o programa encerra
        break
print()
print('   >>> COLETANDO DADOS... AGUARDE <<<   ')
sleep(2)
print('-=' * 30)
print('      >>> DADOS DAS PESSOAS CADASTRADAS <<<   ')
print('-=' * 30)
print()
print(f'   - Foram cadastradas {cont} pessoas.')
print(f'   - A média de idade dessas pessoas é de {sum(idade) / cont} anos.')
print(f'   - As mulheres cadastradas foram {mulheres}.')

for p in dados: # para cada pessoa (p) na lista 'dados'
    if p['Idade'] >= sum(idade) / len(dados): # Se a idade da pessoa for maior ou igual que a soma da idade divido pelo total de pessoas da lista
        print(f'   - Pessoas com idade acima da média: {p["Nome"]} do sexo {p["Sexo"]}, com {p["Idade"]} anos')
print()
print('-=' * 30)
print()
print('<<< FIM >>>')
