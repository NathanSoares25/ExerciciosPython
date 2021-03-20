# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
print('A sua cidade começa com SANTO? Vamos verificar...')
cidade = str(input('Digite o nome da sua cidade: '))
print('SANTO' in cidade.upper().strip().split()[0])
